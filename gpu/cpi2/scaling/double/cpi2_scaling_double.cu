#include <iostream>
#include <stdio.h>
#include <math.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <limits>

static void HandleError(cudaError_t err, const char *file, int line) {
    if (err != cudaSuccess) {
        printf("%s in %s at line %d\n", cudaGetErrorString(err), file, line);
        exit(EXIT_FAILURE);
    }
}

void usage(char * argv[])
{
  printf ("\n%s [-n nblocks]",argv[0]);
  printf ("\n");
}

#define HANDLE_ERROR(err) (HandleError(err, __FILE__, __LINE__))
void usage(char *argv[]);

const int threadsPerBlock = 256;
int nblocks = 128;

__global__ void add(double *res) {
    __shared__ double shr[threadsPerBlock];

    int tid = blockIdx.x * blockDim.x + threadIdx.x;

    double step = 1.0 / (blockDim.x * gridDim.x);
    double x = (tid + 0.5) * step;

    double height = 4 * sqrt(1 - x * x);
    double area = height * step;

    shr[threadIdx.x] = area;

    __syncthreads();

    int i = blockDim.x / 2;
    while (i != 0) {
        if (threadIdx.x < i)
            shr[threadIdx.x] += shr[threadIdx.x + i];
        __syncthreads();
        i /= 2;
    }
    if (threadIdx.x == 0)
        res[blockIdx.x] = shr[threadIdx.x];
}

void options(int argc, char *argv[]) {
    int opt;
    while ((opt = getopt(argc, argv, "n:")) != -1) {
        switch (opt) {
            case 'n':
                nblocks = atoi(optarg);
                break;
            default: /* '?' */
                usage(argv);
                exit(EXIT_FAILURE);
        }
    }
}

int main(int argc, char *argv[]) {
    options(argc, argv);

    double PI = 3.14159265358979323846264338327950288;

    double *res = (double *)malloc(nblocks * sizeof(double));
    double *dev_res;
    HANDLE_ERROR(cudaMalloc((void **)&dev_res, nblocks * sizeof(double)));

    cudaEvent_t start;
    cudaEvent_t stop;
    float msecTotal;

    cudaEventCreate(&start);
    cudaEventRecord(start, NULL);

    add<<<nblocks, threadsPerBlock>>>(dev_res);

    cudaEventCreate(&stop);
    cudaEventRecord(stop, NULL);
    cudaEventSynchronize(stop);

    cudaEventElapsedTime(&msecTotal, start, stop);

    HANDLE_ERROR(cudaMemcpy(res, dev_res, nblocks * sizeof(double), cudaMemcpyDeviceToHost));

    double total = 0;
    for (int i = 0; i < nblocks; i++) {
        total += res[i];
    }

    printf("# Somma %lf\n", total);
    cudaFree(dev_res);

    // Precisione massima possibile
    int precision = std::numeric_limits<double>::digits10;
    fprintf(stderr, "# Numero blocchi, Errore stimato, Tempo di esecuzione\n");
    fprintf(stderr, "%d, %.*e, %f \n", nblocks, precision, fabs(total - PI), msecTotal);

    return 0;
}


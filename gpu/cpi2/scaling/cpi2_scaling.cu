#include <iostream> 
#include <stdio.h>
#include <math.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

static void HandleError( cudaError_t err,
                         const char *file,
                         int line ) {
    if (err != cudaSuccess) {
        printf( "%s in %s at line %d\n", cudaGetErrorString( err ),
                file, line );
        exit( EXIT_FAILURE );
    }
}

#define HANDLE_ERROR( err ) (HandleError( err, __FILE__, __LINE__ ))
void usage(char * argv[]);

const int threadsPerBlock=256;
int nblocks=128;


__global__ void add( float *res ) {
    __shared__ float shr[threadsPerBlock];


    //// qui ogni thread scrive il proprio indice
    //// da modificare con il calcolo del proprio relativo pezzo di rettangoli
    //// utilizzare blockIdx.x, blockDim.x e gridDim.x per calcolare la propria posizione e le divisioni da gestire

    int tid = blockIdx.x * blockDim.x + threadIdx.x;

    // step = 1 / dim tot
    float step = 1.0 / (blockDim.x * gridDim.x);
    float x = (tid + 0.5) * step;

    // Calcolo dell'approssimazione di π utilizzando la formula di Gregory-Leibniz
    // integrale che va da 0 a 1 di 1/(1+ x^2) = π/4
    //float height = (4.0f / (1.0f + x*x));
    float height = 4 * sqrt(1-x*x);


    // L'area del rettangolo
    float area = height * step;

    shr[threadIdx.x] = area;

    //shr[threadIdx.x]=threadIdx.x;

    __syncthreads();

    // for reductions, threadsPerBlock must be a power of 2 // because of the following code
    int i = blockDim.x/2;
    while (i != 0) {
            if (threadIdx.x < i)
        shr[threadIdx.x] += shr[threadIdx.x + i];
        __syncthreads();
        i /= 2;
    }
    if (threadIdx.x==0)
    res[blockIdx.x] = shr[threadIdx.x];
}

// funzione che gestisce flag di input

void options(int argc, char *argv[])
{
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

int main( int argc, char *argv[] ) { 

    options(argc, argv);

    double  PI = 3.14159265358979323846264338327950288;

    float* res=(float*)malloc(nblocks*sizeof(float));
    float *dev_res;
    HANDLE_ERROR( cudaMalloc( (void**)&dev_res, nblocks*sizeof(float) ) );
    //printf("# start\n");

    // calcolo tempo di esecuzione con cudaEvents
    cudaEvent_t start;
    cudaEvent_t stop;
    float msecTotal;

    cudaEventCreate(&start);
    cudaEventRecord(start, NULL); 

    add<<<nblocks,threadsPerBlock>>>( dev_res );

    cudaEventCreate(&stop);
    cudaEventRecord(stop, NULL);
    cudaEventSynchronize(stop);

    cudaEventElapsedTime(&msecTotal, start, stop);

    HANDLE_ERROR( cudaMemcpy( res, dev_res, nblocks*sizeof(float), cudaMemcpyDeviceToHost ) ); 
    
    

    float total=0;
    for (int i=0;i<nblocks;i++){
      //printf("# Block %d: %f\n",i,res[i]);
      total+=res[i];
    }

    printf("# Somma %f\n",total);
    cudaFree( dev_res );

    //Numero blocchi, Errore stimato, Tempo di esecuzione divisi da una virgola in stderr
    fprintf(stderr, "# Numero blocchi, Errore stimato, Tempo di esecuzione, somma\n");
    fprintf(stderr, "%d, %lf, %f, %f\n", nblocks, fabs(total-PI), msecTotal, total);
    
    return 0; 
}

void usage(char * argv[])
{
  printf ("\n%s [-n nblocks]",argv[0]);
  printf ("\n");
}

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/bn.h>
#include <math.h>
#include <omp.h>
#include <stdbool.h>

void status() {}
void options(int argc, char *argv[]);
void usage(char *argv[]);
int block_factorize(unsigned long int);

BIGNUM *P, *Q, *M, *F, *ZERO, *ONE, *TWO, *BLOCK_DIM_SIZE, *BLOCK_DIM_BIT;
BN_CTX *ctx;
int block_idx = 0, block_found;
int thr=0;
unsigned long int modulus_bit, prime_bit, block_addr_bit, block_addr_size, block_dim_bit, block_dim_size;


//char m[256] = "97219FA6BD3D7735"; // 64 bit
//char m[256]="B81915BC0A2222F4B";        // 68 bit
//char m[256]="F27F04CC3A51A3090B7D";     // 80 bit
char m[256]="CD2C32D00F3E6CC158F1E069"; // 96 bit

int main(int argc, char *argv[])
{
    int i;
    float t1, t2; // timer
    bool skip = false;
    omp_set_nested(1);

    // BN setting
    P = BN_new();                 // prime number
    Q = BN_new();                 // prime number
    M = BN_new();                 // modulus = p x q
    F = BN_new();                 // found number
    ZERO = BN_new();              // 0
    ONE = BN_new();               // 1
    TWO = BN_new();               // 2
    BLOCK_DIM_BIT = BN_new();     // quanti bit per blocco
    BLOCK_DIM_SIZE = BN_new();    // dimensione blocco
    ctx = BN_CTX_new();
    BN_set_word(ZERO, 0);
    BN_set_word(ONE, 1);
    BN_set_word(TWO, 2);

    // Default values
    modulus_bit = 64; // init modulus bits
    block_addr_bit = 4;
    //printf("Default modulus_bit %d\n", modulus_bit);

    // Options management
    options(argc, argv);

    //printf("Modulus_bit scelto per l'esecuzione %d\n", modulus_bit);

    BN_hex2bn(&M, m);
    modulus_bit = strlen(m) * 4;
    prime_bit = modulus_bit / 2;
    block_dim_bit = prime_bit - block_addr_bit;
    block_dim_size = pow(2, block_dim_bit);

    BN_set_word(BLOCK_DIM_BIT, block_dim_bit);                 // bits per block
    BN_exp(BLOCK_DIM_SIZE, TWO, BLOCK_DIM_BIT, ctx);

    printf("\n# Modulus: ");
    BN_print_fp(stdout, M);
    printf(" %d bits - prime %d bit: address %d bit, block %d bit \n\n", modulus_bit, prime_bit, block_addr_bit, block_dim_bit);

    printf("Numero di thread: %d\n", thr);

    t1 = omp_get_wtime();
    if (thr) omp_set_num_threads(thr);

    #pragma omp parallel for shared(skip)
    for (block_idx = pow(2, block_addr_bit) - 1; block_idx >= 0; block_idx--)
    {
        if (skip)
            continue;

        if (block_factorize(block_idx))
        {   
            #pragma omp critical
            skip = true;

            printf("Block %d - FOUND - Thread %d. ", block_idx, omp_get_thread_num());
            BN_print_fp(stdout, F);
            printf("\n");
        }
        else
        {   if (skip)
            printf("Thread %d Skip \n", omp_get_thread_num());
            else
            // dico che non ho trovato il blocco e che thread sono
            printf("Block %d - NOT FOUND - Thread %d\n", block_idx, omp_get_thread_num());
        }
    }

    t2 = omp_get_wtime();
    printf("Time: %.1f secondi \n", t2 - t1);

    return 0;
}

int block_factorize(unsigned long int block_addr)
{
    BIGNUM *R, *X, *Y, *BLOCK_IDX, *BLOCK_ADDR;
    BN_CTX *ctx2;
    ctx2 = BN_CTX_new();
    R = BN_new();          // resto della divisione
    X = BN_new();          // indice del blocco
    Y = BN_new();          // ultimo numero del blocco
    BLOCK_IDX = BN_new();  // ultimo numero del blocco
    BLOCK_ADDR = BN_new(); // Block Address

    BN_set_word(R, 0);
    BN_set_word(X, 1);
    BN_set_word(Y, 1);
    BN_set_word(BLOCK_ADDR, block_addr);
    BN_mul(X, BLOCK_ADDR, BLOCK_DIM_SIZE, ctx2); // x = i  block_size
    BN_add(X, X, ONE);                            // x = x+1
    BN_add(Y, X, BLOCK_DIM_SIZE);                 // y = x + block_size
    BN_sub(Y, Y, TWO);                            // y = y - 2
    BLOCK_IDX = BN_dup(X);

    while (BN_cmp(BLOCK_IDX, Y))
    {
        BN_add(BLOCK_IDX, BLOCK_IDX, TWO);
        BN_mod(R, M, BLOCK_IDX, ctx2);
        if (BN_is_zero(R))
        {
            F = BN_dup(BLOCK_IDX);
            return 1;
        }
    }

    return 0;
}

void options(int argc, char * argv[])
{
  int i;
   while ( (i = getopt(argc, argv, "a:t:b:m:h")) != -1) {
        switch (i)
        {
        case 't':  thr            = strtol(optarg, NULL, 10);  break;
        case 'a':  block_addr_bit = strtol(optarg, NULL, 10);  break;
        case 'b':  modulus_bit    = strtol(optarg, NULL, 10);  break;
        case 'm':  strcpy(m,optarg);  break;
        case 'h':  usage(argv); exit(1);
        case '?':  usage(argv); exit(1);
        default:   usage(argv); exit(1);
        }
    }
}

void usage(char *argv[])
{
    printf("\n%s [-b modulus_bit] [-m modulus] [-a block_addr_bit] [-h]", argv[0]);
    printf("\n");
}

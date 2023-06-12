
/* gcc factorize1.c -o factorize1 -lcrypto -lm */

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/bn.h>
#include <math.h>
#include <omp.h>

void status() {}
int block_factorize (unsigned long int);

BIGNUM *P, *Q, *M, *F, *ZERO,  *ONE, *TWO, *BLOCK_SIZE, *BLOCK_SIZE_BIT ;
BN_CTX *ctx;
int block_idx, found=0; 
unsigned long int  block_size_bit, block_size, block_num_bit, block_num ;  


int main(int argc, char *argv[])
{

        double t1, t2; // timer
        unsigned long int nbits;
        if(argc >= 2 && argv[1]) nbits          = atol(argv[1]);
        else  nbits = 24;
        if(argc >= 3 && argv[2]) block_size_bit = atol(argv[2]);
        else block_size_bit = 20;         

        P = BN_new();     // prime number
        Q = BN_new();     // prime number
        M = BN_new();     // modulw = p x q
        F = BN_new();     // found number

        ZERO           = BN_new();  //  0
        ONE            = BN_new();  //  1
        TWO            = BN_new();  //  2
        BLOCK_SIZE_BIT = BN_new();  // quanti bit per blocco  
        BLOCK_SIZE     = BN_new();  // dimensione blocco 
        ctx = BN_CTX_new();

        block_num_bit = nbits - block_size_bit;                 
        block_num     = pow(2,block_num_bit);

        BN_set_word(ZERO,0);
        BN_set_word(ONE,1);
        BN_set_word(TWO,2);
        BN_set_word(BLOCK_SIZE_BIT,block_size_bit);                 // bits per block
        BN_exp(BLOCK_SIZE, TWO , BLOCK_SIZE_BIT,ctx);

        printf(" # BLOCK_SIZE_BIT: ");
        BN_print_fp(stdout,  BLOCK_SIZE_BIT);
        printf("  ");
        printf(" BLOCK_SIZE:");
        BN_print_fp(stdout, BLOCK_SIZE);
        printf("\n");

        BN_generate_prime(P,nbits,1,NULL,NULL,status,NULL);
        BN_generate_prime(Q,nbits,1,NULL,NULL,status,NULL);
        BN_mul(M,P,Q, ctx); 

        printf("\n #P : ");
        BN_print_fp(stdout,P);
        printf("\n #Q : ");
        BN_print_fp(stdout,Q);
        printf("\n #M : ");
        BN_print_fp(stdout,M);
        printf("\n");

        #pragma omp parallel private(block_idx) shared(found) num_threads(2)
        {
          #pragma omp sections
          {
          #pragma omp section
            {
              printf("Master %d/%d \n",omp_get_thread_num(),omp_get_num_threads() );
            }

          #pragma omp section
            {
              #pragma omp parallel
              for (block_idx=block_num-1; block_idx > -1 ; block_idx--)
                block_factorize (block_idx);
            }

          } // end sections
        } // end parallel
        

        printf("FOUND: ");
        BN_print_fp(stdout,F);
        printf("\n");
        return (0);
}


int block_factorize (unsigned long int block_idx)
{

              BIGNUM *R, *X, *Y, *BLOCK_IDX;
              BN_CTX *ctx2;
              R       = BN_new();  // resto della divisione
              X       = BN_new();  // indice del  blocco
              Y       = BN_new();  // ultimo numero del  blocco
              BLOCK_IDX       = BN_new();  // ultimo numero del  blocco
              ctx2 = BN_CTX_new();

              BN_set_word(R,0);
              BN_set_word(X,1);
              BN_set_word(Y,1);
              BN_set_word(BLOCK_IDX, block_idx);

              BN_mul(X, BLOCK_IDX, BLOCK_SIZE,ctx2);       // x = i  block_size
              BN_add(X,X,ONE);                             // x = x+1 
              BN_add(Y,X,BLOCK_SIZE);                      // y = x + block_size

              while ( ! found  && BN_cmp(X,Y))
                {
                BN_add(X,X,TWO);
                BN_mod(R,M,X, ctx2);
                if ( BN_is_zero(R) ) 
                  { 
                    F=BN_dup(X);
                    found=1;
                  }  
               }

              printf("# BLOCK_IDX:");
              BN_print_fp(stdout,BLOCK_IDX);
              printf(" startX:");
              BN_print_fp(stdout, X);
              printf(" lastX:");
              BN_print_fp(stdout, Y);   
              if (found) printf (" found \n");  else  printf (" not found \n"); 
   
               return (0);
}

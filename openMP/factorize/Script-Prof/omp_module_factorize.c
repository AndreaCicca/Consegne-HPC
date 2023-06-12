
/* g++ -fopenmp omp_module_factorize.c -o omp_module_factorize -lgmp */

#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <omp.h>
#include <time.h>

#define CHUNK_SIZE_HEX 0x200000
#define INCR 2UL

int main(int argc, char *argv[])
{
    const size_t chunk_size = CHUNK_SIZE_HEX;

    // p, q, modulo variables
    mpz_t p, q, m;

    long int num_bits = 0;
    if(argc >= 2 && argv[1])
        num_bits = atol(argv[1]);
    else
        num_bits = 1024;

  printf("num_bits: %d\n", num_bits); 
   
    // Initializing variables
    mpz_init(p);
    mpz_init(q);
    mpz_init(m);

   
    // seed random function
    gmp_randstate_t state;
    gmp_randinit_default(state);
    gmp_randseed_ui(state, time(NULL));

    // Generate random primes
    mpz_urandomb(p, state, num_bits);
    mpz_nextprime(p, p);

    mpz_urandomb(q, state, num_bits);
    mpz_nextprime(q, q);

    // Print primes to screen
    gmp_printf("p: %Zd\nq: %Zd\n", p, q);

    // Calculate modulo
    mpz_mul(m, p, q);
    gmp_printf("m: %Zd\n", m);

    
    // Get the number of threads
    int num_threads = omp_get_max_threads();
    printf("Number of threads : %d\n", num_threads);
    printf("Chunk size : %lu\n", chunk_size);
    
    // Allocate arrays of x and rem for each running core
    mpz_t *x = (mpz_t*) malloc(num_threads * sizeof(mpz_t));
    mpz_t *rem = (mpz_t*) malloc(num_threads * sizeof(mpz_t));
    
    // Set the corresponding starting chunk to each core
    for (size_t i = 0; i < num_threads; i++) {
        mpz_init(x[i]);
        mpz_set_ui(x[i], 1 + chunk_size*i);
        mpz_init(rem[i]);
        mpz_set_ui(rem[i], 1);
    }
    
    // Initialize exit condition variable
    int found = -1;

    #pragma omp parallel shared(found) num_threads(num_threads)
    {
    	// Get local rank
    	int tid = omp_get_thread_num();
    	
    	
    	// Skip summation for the first iteration
	switch (1)
	{
    	while (found == -1)
    	{	
    		// Get next chunk
		mpz_add_ui(x[tid], x[tid], chunk_size*(num_threads-1));

	default:
	
		// Search the current chunk
    		for (size_t i=0; i<chunk_size; i+=INCR)
    		{
    			mpz_add_ui(x[tid], x[tid], INCR);
            		mpz_mod(rem[tid], m, x[tid]);
            		
            		// If a factor is found, print own rank in found variable
            		// to signal computation end
            		if (mpz_cmp_ui(rem[tid], 0UL) == 0)
            		{
	    			#pragma omp critical
	    			{
	    				found = tid;
		    		}
		    		
            			break;
                    	}
    		}
    		
     	}
	}
    }
    
    // Print result
    gmp_printf("FOUND: %Zd\n", x[found]);
    
    // Clear memory
    mpz_clear(p);
    mpz_clear(q);
    mpz_clear(m);
    
    for (size_t i = 0; i < num_threads; i++)
    {
        mpz_clear(x[i]);
        mpz_clear(rem[i]);
    }
    
    free(x);
    free(rem);

    gmp_randclear(state);
    
    return 0;
}


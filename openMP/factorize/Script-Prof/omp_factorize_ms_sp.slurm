#!/bin/bash


#SBATCH --output=%x.o%j-80bit
#SBATCH --partition=cpu_guest
#SBATCH --qos=cpu_guest
#SBATCH -n 8
#SBATCH --time=0-23:10:00

module load gnu8
gcc omp_factorize_ms_sp.c -o omp_factorize_ms_sp   -lcrypto -lm -fopenmp 


./omp_factorize_ms_sp -m  E89E4058B29266870335 -a 8    #modulus 80 bit, prime 40 bit (8 addr, 32 block)

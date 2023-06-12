#!/bin/bash
#SBATCH --output=%x.o%j-80bit
#SBATCH --partition=cpu_guest
#SBATCH --qos=cpu_guest
#SBATCH -n 8
#SBATCH --time=0-23:10:00

module load gnu8
gcc omp_factorize_master_slave.c -o omp_factorize_master_slave   -lcrypto -lm -fopenmp 

for T in 8 4 2 1
do

#./omp_factorize2 -t $T -m  C1107FA48AE45B16C3  -a 4     #modulus 72 bit, prime 36 bit (4 addr, 32 block)
./omp_factorize_master_slave -t $T -m   E89E4058B29266870335 -a 8    #modulus 80 bit, prime 40 bit (8 addr, 32 block)
#./omp_factorize2 -t $T -m  D41EEDCA71F14147E3F7A1FD          #modulus 96 bit
#./omp_factorize2 -t $T -m  B686C5D7A74B840E8B27F840126367F5  #modulus 128 bit
done 

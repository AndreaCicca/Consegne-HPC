#!/bin/bash
#SBATCH --output=%x.o%j-64
#SBATCH --partition=cpu_guest
#SBATCH --qos=cpu_guest
#SBATCH -n 8
#SBATCH --time=0-23:10:00

#gcc omp_factorize2.c -o omp_factorize2   -lcrypto -lm -fopenmp 

for T in  1 2 4 8
do
#./omp_factorize2 -t $T  -m  B686C5D7A74B840E8B27F840126367F5 #128 bit
#./omp_factorize2 -t $T  -m  D41EEDCA71F14147E3F7A1FD         #96 bit
./omp_factorize2 -t $T -m  B7D4AA3A02A2CA4D                 #64 bit
done 

#!/bin/bash
#SBATCH --output=%x.o%j-96bit
#SBATCH --partition=cpu_guest
#SBATCH --qos=cpu_guest
#SBATCH --cpus-per-task=64
#SBATCH --time=0-06:10:00

#time ./omp_factorize2 -t 8 -m C9C672F60FF7C2DA0E419744E7071929
#time ./omp_factorize_master_slave -t 8 -m C9C672F60FF7C2DA0E419744E7071929
#time ./omp_factorize3 -t 8 -m C9C672F60FF7C2DA0E419744E7071929
time ./omp_factorize3 -m CD2C32D00F3E6CC158F1E069 -t 64
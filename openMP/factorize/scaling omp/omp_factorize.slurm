#!/bin/bash
#SBATCH --output=%x.o%j-64bit
#SBATCH --partition=cpu_guest
#SBATCH --qos=cpu_guest
#SBATCH --cpus-per-task=64
#SBATCH --time=0-06:00:00
#SBATCH --mem=16

module purge
module load gnu8

# elimino master-slave.dat se esiste
rm -f omp-scaling.dat

for T in 8 16 32 64
do

# stampo T in master-slave.dat con uno spazio dopo
echo -n "$T " >> omp-scaling.dat

./omp_factorize2 -t $T -m  B7D4AA3A02A2CA4D
done 


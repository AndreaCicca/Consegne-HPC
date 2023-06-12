#!/bin/bash
#SBATCH --output=%x.o%j-128bit
#SBATCH --partition=cpu_guest
#SBATCH --qos=cpu_guest
#SBATCH --cpus-per-task=64
#SBATCH --time=0-12:10:00

module purge
module load gnu8

for T in 64
do
time ./omp_factorize2 -t $T -m  B686C5D7A74B840E8B27F840126367F5  #modulus 128 bit
done 

# Delle considerazioni su questo slurm si trovano alla fine del file factorize.txt
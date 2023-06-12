#!/bin/bash
#SBATCH --output=%x.o%j
##SBATCH --error=%x.e%j
#SBATCH --partition=cpu_guest
#SBATCH --qos=cpu_guest
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --time=23-00:00:00

echo "Thread,nx,ny,iter,T,Tp,Tnp" > omp_heat.dat
echo "Thread,nx,ny,iter,T,Tp,Tnp" > omp_heat_gnu8.dat
echo "Thread,nx,ny,iter,T,Tp,Tnp" > omp_heat_intel.dat

#GNU4

module purge

gcc -fopenmp -O3 -o omp_heat omp_heat.c

for T  in   1 2 4 8
do

echo -n "$T," >> omp_heat.dat

OMP_NUM_THREADS=$T ./omp_heat -c 2048 -r 2048 1> /dev/null 2>> omp_heat.dat

done

#GNU8

module purge
module load gnu8

gcc -fopenmp -O3 -o omp_heat_gnu8 omp_heat.c

for T  in   1 2 4 8
do

echo -n "$T," >> omp_heat_gnu8.dat

OMP_NUM_THREADS=$T ./omp_heat_gnu8 -c 2048 -r 2048 1> /dev/null 2>> omp_heat_gnu8.dat

done

#INTEL

module purge
module load intel openmpi/2.1.2

icc -qopenmp -O3 -o omp_heat_intel omp_heat.c

for T  in   1 2 4 8
do

echo -n "$T," >> omp_heat_intel.dat

OMP_NUM_THREADS=$T ./omp_heat_intel -c 2048 -r 2048 1> /dev/null 2>> omp_heat_intel.dat

done

module purge

python2.7 confronto_plot.py


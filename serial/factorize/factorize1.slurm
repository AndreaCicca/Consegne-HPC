#!/bin/bash
##SBATCH --output=output-20bit.out
#SBATCH --partition=cpu_guest
#SBATCH --qos=cpu_guest
#SBATCH --output=%x.o%j

#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=0-00:30:00


echo "#SLURM_JOB_NODELIST: $SLURM_JOB_NODELIST"

gcc factorize1.c -o factorize1 -lcrypto  -lm


time ./factorize1 24

#!/bin/bash

#SBATCH --output=%x.o%j  # Nome del file per lo strandard output
##SBATCH --error=%x.e%j  # Se non specificato stderr e' rediretto su stdout
#SBATCH --partition=cpu_guest              # Nome della partizione, cpu per job paralleli
#SBATCH --qos=cpu_guest              # 
#SBATCH --nodes=1                    # numero di nodi richiesti
#SBATCH --cpus-per-task=1            # numero di cpu 
##SBATCH --mem=2G                    # massima memoria utilizzata
#SBATCH --time=0-10:10:00            # massimo tempo di calcolo

gcc factorize0.c -o factorize0 -O2 -lcrypto

time ./factorize0 24

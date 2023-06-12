#!/bin/sh
 
# Richiedi un nodo con una gpu
#SBATCH --output=slurm_cpi2_scaling_double.out
#SBATCH --partition=gpu
#SBATCH --nodes=1 
#SBATCH --mem=4G

#SBATCH --qos=gpu
#SBATCH --gres=gpu:p100:1

# Dichiara che il job durera' al massimo 1 minuto
#SBATCH --time=0-00:01:00

#stampa il nome del nodo assegnato e argomenti                 
echo "#SLURM_JOB_NODELIST   : $SLURM_JOB_NODELIST"
echo "#CUDA_VISIBLE_DEVICES : $CUDA_VISIBLE_DEVICES"

#esegui il programma
module purge
module load cuda 
nvcc -arch=sm_60 cpi2_scaling_double.cu -o cpi2_scaling_double

rm -f cpi2_scaling_double.dat output_scaling_double.csv
touch cpi2_scaling_double.dat
echo "Numero blocchi, Errore stimato, Tempo di esecuzione" >> cpi2_scaling_double.dat

for i in 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144
do  
    echo "# Esecuzione blocco $i"
    ./cpi2_scaling_double -n $i 2>> cpi2_scaling_double.dat
done

cat cpi2_scaling_double.dat | fgrep -v "#"  > output_scaling_double.csv


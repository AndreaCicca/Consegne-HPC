#!/bin/sh
 
# Richiedi un nodo con una gpu
#SBATCH --output=%x.o%j-P100
##SBATCH --partition=gpu_guest
#SBATCH --partition=gpu
#SBATCH --nodes=1 
#SBATCH --mem=4G

#SBATCH --qos=gpu
#SBATCH --gres=gpu:p100:1

# Dichiara che il job durera' al massimo 1 minuto
#SBATCH --time=0-00:04:00
##SBATCH --reservation=t_2022_hpcprogpar_20230601

#stampa il nome del nodo assegnato e argomenti                 
echo "#SLURM_JOB_NODELIST   : $SLURM_JOB_NODELIST"
echo "#CUDA_VISIBLE_DEVICES : $CUDA_VISIBLE_DEVICES"

module load cuda/11.6.0

nvcc -O2  heat_gpu.cu -o heat_gpu

# Se già presente elimino la cartella ./output e tutto il suo contenuto
rm -rf ./output

mkdir -p ./output


# for loop della dimensione del blocco
for N in 4 8 16 32
do

nvcc -O2 -DBLOCK_SIZE_Y=$N -DBLOCK_SIZE_X=$N heat_gpu.cu -o heat_gpu
# scrivo in output "eseguita compilazione grandezza blocco $N"
echo "eseguita compilazione grandezza blocco $N"

# for loop dimensione delle matrici
for M in 64 128 256 512 1024 2048
do
heat_gpu -c $M -r $M  -s 100000 2>> ./output/output_$N.dat

done

done

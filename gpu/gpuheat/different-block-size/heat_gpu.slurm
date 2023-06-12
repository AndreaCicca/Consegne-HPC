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
#SBATCH --time=0-00:01:00
##SBATCH --reservation=t_2022_hpcprogpar_20230601

#stampa il nome del nodo assegnato e argomenti                 
echo "#SLURM_JOB_NODELIST   : $SLURM_JOB_NODELIST"
echo "#CUDA_VISIBLE_DEVICES : $CUDA_VISIBLE_DEVICES"

module load cuda/11.6.0



nvcc -O2  heat_gpu.cu -o heat_gpu

for N in 4 8 16 32
do
nvcc -O2 -DBLOCK_SIZE_Y=$N -DBLOCK_SIZE_X=$N heat_gpu.cu -o heat_gpu
heat_gpu  -c 512 -r 512  -s 100000 2>>output.dat

done

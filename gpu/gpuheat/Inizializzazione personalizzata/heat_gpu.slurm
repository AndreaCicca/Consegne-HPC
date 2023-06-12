#!/bin/sh
 
# Richiedi un nodo con una gpu
##SBATCH --partition=gpu_guest
#SBATCH --output=output.out
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

module load cuda/11.6.0

nvcc -O2  heat_gpu_inizializzazione_perosnalizzata.cu -o heat_gpu 

./heat_gpu  -c 1024 -r 1024  -s 100000

# cat output.out | fgrep -v "#"  > my_file.csv ; python heat_plot.py my_file.csv
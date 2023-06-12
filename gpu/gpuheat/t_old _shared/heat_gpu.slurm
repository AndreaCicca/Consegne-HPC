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
#SBATCH --time=0-00:15:00

#stampa il nome del nodo assegnato e argomenti                 
echo "#SLURM_JOB_NODELIST   : $SLURM_JOB_NODELIST"
echo "#CUDA_VISIBLE_DEVICES : $CUDA_VISIBLE_DEVICES"

module load cuda/11.6.0

rm -rf ./output

mkdir -p ./output

echo "# Inizio compilazione"

nvcc -O2  heat_gpu_shared.cu -o heat_gpu_shared
nvcc -O2  heat_gpu.cu -o heat_gpu

echo "# Fine compilazione"

for N in 64 128 256 512 1024
do
    echo "# N=$N"
    heat_gpu  -c $N -r $N  -s 100000 2>>output/heat_standard.dat
    heat_gpu_shared -c $N -r $N -s 100000 2>>output/heat_shared.dat
done



echo "# Fine esecuzione"

# cat output.out | fgrep -v "#"  > my_file.csv ; python heat_plot.py my_file.csv

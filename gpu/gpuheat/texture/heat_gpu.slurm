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
#SBATCH --time=0-00:04:00

#stampa il nome del nodo assegnato e argomenti                 
echo "#SLURM_JOB_NODELIST   : $SLURM_JOB_NODELIST"
echo "#CUDA_VISIBLE_DEVICES : $CUDA_VISIBLE_DEVICES"

module load cuda/11.6.0

rm -rf ./output

mkdir -p ./output

nvcc -O2  heat_gpu_texture.cu -o heat_gpu_texture 2> warnings.txt
nvcc -O2  heat_gpu.cu -o heat_gpu

for N in 64 128 256 512 1024 2048 4096
do
    echo "# N=$N"
    heat_gpu  -c $N -r $N  -s 100000 2>>output/heat_standard.dat
    heat_gpu_texture -c $N -r $N -s 100000 2>>output/heat_texture.dat
done

#cat output.out | fgrep -v "#"  > my_file.csv ; python heat_plot.py my_file.csv
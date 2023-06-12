#!/bin/bash


echo "function,iter,pi,error,t_np,t_p,hostname" > cpi_scaling_f1.csv
echo "function,iter,pi,error,t_np,t_p,hostname" > cpi_scaling_f2.csv

for N in $(seq 1000000 100000 9000000)
#for N  in  1000 2000 3000
do
./cpi_f1 -n $N  >> cpi_scaling_f1.csv
done

for N in $(seq 1000000 100000 9000000)
#for N  in  1000 2000 3000
do
./cpi_f2 -n $N  >> cpi_scaling_f2.csv
done

python2.7 cpi_scaling_plot.py

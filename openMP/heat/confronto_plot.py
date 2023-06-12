import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import pandas as pd 
import info_personali as ip
import sys

# I miei dati sono del tipo 

# Thread,nx,ny,iter,T,Tp,Tnp
# 1,2048, 2048, 1000, 1.943, 1.877, 0.066 
# 2,2048, 2048, 1000, 1.656, 1.551, 0.105 
# 4,2048, 2048, 1000, 0.969, 0.893, 0.076 
# 8,2048, 2048, 1000, 1.024, 0.941, 0.083 

# Il nume del file deriva dal primo parametro passato allo script

# Mi salvo il primo parametro

omp = pd.read_csv('omp_heat.dat',sep=',',header=0)
omp_gnu8 = pd.read_csv('omp_heat_gnu8.dat',sep=',',header=0)
omp_intel = pd.read_csv('omp_heat_intel.dat',sep=',',header=0)

plt.title('OMP Heat TP VS TNP (gnu4) -  ' + ip.get_user() + '  ' + ip.get_timestamp())
plt.grid()
plt.xlabel('n thread')
plt.ylabel('tempo')
plt.plot(omp.Thread,omp.Tnp,'g-^',label='Tempo seriale')
plt.plot(omp.Thread,omp.Tp,'y-^',label='Tempo parallelo')
plt.legend(shadow=True,loc='upper right')
plt.savefig('omp_heat.png')

plt.clf()

# confronto tra i compilatori

plt.title('OMP Heat Confronto -  ' + ip.get_user() + '  ' + ip.get_timestamp())
plt.grid()
plt.xlabel('n thread')
plt.ylabel('tempo')
plt.yscale('log')
plt.plot(omp.Thread,omp.Tp,'y-^',label='Tempo parallelo gnu4')
plt.plot(omp_gnu8.Thread,omp_gnu8.Tp,'g-^',label='Tempo parallelo gnu8')
plt.plot(omp_intel.Thread,omp_intel.Tp,'r-^',label='Tempo parallelo intel19')

plt.legend(shadow=True,loc='upper right')

plt.savefig('omp_heat_compilatori_confronto.png')
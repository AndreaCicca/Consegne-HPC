import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import pandas as pd 
import info_personali as ip

cpi1 = pd.read_csv("cpi_scaling_f1.csv") 
cpi2 = pd.read_csv("cpi_scaling_f2.csv") 


plt.title('cpi Parallelo  Legge di Amdahl  -  ' + ip.get_user() + '  ' + ip.get_timestamp())
plt.grid()
plt.xscale('log')
plt.xlabel('Intervalli')
plt.ylabel('tempo')
plt.plot(cpi1.iter,cpi1.t_p,'g-^',label='f1() - Tempo parallelo')
plt.plot(cpi2.iter,cpi2.t_p,'y-^',label='f2() - Tempo parallelo')
plt.legend(shadow=True,loc='upper left')
plt.savefig('confronto_Tparallelo.png')

plt.clf()


plt.title('cpi Seriale  Legge di Amdahl  -  ' + ip.get_user() + '  ' + ip.get_timestamp())
plt.grid()
plt.xscale('log')
#plt.yscale('log')
plt.xlabel('Intervalli')
#plt.yscale('log')
plt.ylabel('tempo')
plt.plot(cpi1.iter,cpi1.t_np,'r-o',label='f1() - T non parallelo')
plt.plot(cpi2.iter,cpi2.t_np,'b-o',label='f2() - T non parallelo')
plt.legend(shadow=True,loc='upper left')
plt.savefig('confronto_Tseriale.png')

plt.clf()

plt.title('cpi Quota parallela Legge di Amdahl - ' + ip.get_user() + ' ' + ip.get_timestamp())
plt.grid()
plt.xscale('log')
#plt.yscale('log')
plt.xlabel('Intervalli')
#plt.yscale('log')
plt.ylabel('quota')

# Nota bene Qp=Tp/(Tnp+Tp)

plt.plot(cpi1.iter,cpi1.t_p/(cpi1.t_p+cpi1.t_np),'g-^',label='f1() - Q parallela')
plt.plot(cpi2.iter,cpi2.t_p/(cpi2.t_p+cpi2.t_np),'y-^',label='f2() - Q parallela')
plt.legend(shadow=True,loc='upper left')
plt.savefig('confronto_Qp.png')

plt.clf()

plt.title('cpi Quota seriale  Legge di Amdahl - ' + ip.get_user() + ' ' + ip.get_timestamp())
plt.grid()
plt.xscale('log')
#plt.yscale('log')
plt.xlabel('Intervalli')
#plt.yscale('log')
plt.ylabel('quota')

# Nota bene Qnp= Tnp/(Tnp+Tp)
plt.plot(cpi1.iter,cpi1.t_np/(cpi1.t_p+cpi1.t_np),'r-o',label='f1() - Quota non parallela')
plt.plot(cpi2.iter,cpi2.t_np/(cpi2.t_p+cpi2.t_np),'b-o',label='f2() - Quota non parallela')
plt.legend(shadow=True,loc='upper left')
plt.savefig('confronto_Qnp.png')
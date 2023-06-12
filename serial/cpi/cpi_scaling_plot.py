import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import pandas as pd 
import info_personali as ip

cpi_1 = pd.read_csv("cpi_scaling_f1.csv") 
cpi_2 = pd.read_csv("cpi_scaling_f2.csv")

# Plot con la funzione f1

plt.title('cpi f1  Legge di Amdahl  -  ' + ip.get_user() + '  ' + ip.get_timestamp())
plt.grid()
plt.xlabel('Intervalli')
plt.yscale('log')
plt.ylabel('tempo')
plt.plot(cpi_1.iter,cpi_1.t_np,'r-o',label='T non parallelo')
plt.plot(cpi_1.iter,cpi_1.t_p,'g-o',label='T parallelo')
plt.legend(shadow=True)
plt.savefig('cpi_scaling_tempo_f1.png')

plt.clf()

plt.title('cpi f1  Legge di Amdahl  -  ' + ip.get_user() + '  ' + ip.get_timestamp())
plt.grid()
plt.xlabel('Intervalli')
plt.yscale('log')
plt.ylabel('quote')
plt.plot(cpi_1.iter,cpi_1.t_np/(cpi_1.t_p+cpi_1.t_np),'r-o',label='Quota non parallela')
plt.plot(cpi_1.iter,cpi_1.t_p/(cpi_1.t_p+cpi_1.t_np),'g-o',label='Quota parallela')
plt.legend(shadow=True)
plt.savefig('cpi_scaling_quote_f1.png')

# Plot con la funzione f2
plt.clf()

plt.title('cpi f2  Legge di Amdahl  -  ' + ip.get_user() + '  ' + ip.get_timestamp())
plt.grid()
plt.xlabel('Intervalli')
plt.yscale('log')
plt.ylabel('tempo')
plt.plot(cpi_2.iter,cpi_2.t_np,'r-o',label='Tempo non parallelo')
plt.plot(cpi_2.iter,cpi_2.t_p,'g-o',label='Tempp parallelo')
plt.legend(shadow=True)
plt.savefig('cpi_scaling_tempo_f2.png')

plt.clf()

plt.title('cpi f2 Legge di Amdahl  -  ' + ip.get_user() + '  ' + ip.get_timestamp())
plt.grid()
plt.xlabel('Intervalli')
plt.yscale('log')
plt.ylabel('quote')
plt.plot(cpi_2.iter,cpi_2.t_np/(cpi_2.t_p+cpi_2.t_np),'r-o',label='Quota non parallela')
plt.plot(cpi_2.iter,cpi_2.t_p/(cpi_2.t_p+cpi_2.t_np),'g-o',label='Quota parallela')
plt.legend(shadow=True)
plt.savefig('cpi_scaling_quote_f2.png')
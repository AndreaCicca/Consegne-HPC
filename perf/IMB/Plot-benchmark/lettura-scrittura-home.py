import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import pandas as pd 

imb_lettura_home = pd.read_csv("./dat-file/IMB-IO-S_Read-indv.dat",comment="#", sep='\s+',  names=["bytes", "repetitions","time","MBps"] )
imb_scrittura_home = pd.read_csv("./dat-file/IMB-IO-S_Write-indv.dat",comment="#", sep='\s+',  names=["bytes", "repetitions","time","MBps"] )


# Confronto della banda (Mbyes/s) tra SHM, OPA e IB al crescere della dimensione dei messaggi 
plt.title('Confronto velocità scrittura/lettura (Mbyes/s)')
plt.grid()
plt.xlabel('Grandezza messaggio in bytes')
plt.ylabel('(Mbyes/s)')
plt.xscale('log')

plt.plot(imb_lettura_home.bytes,imb_lettura_home.MBps,'ro',label='Lettura', linewidth=2, linestyle='-')
plt.plot(imb_scrittura_home.bytes,imb_scrittura_home.MBps,'bo',label='Scrittura', linewidth=2, linestyle='-')

#print(lettura)

plt.legend(shadow=True)
plt.savefig('./output-plot/confronto-lettura-scrittura.png')


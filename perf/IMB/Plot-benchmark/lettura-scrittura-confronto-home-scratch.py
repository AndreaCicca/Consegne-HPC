import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import pandas as pd 

imb_lettura_home = pd.read_csv("./dat-file/IMB-IO-S_Read-indv.dat",comment="#", sep='\s+',  names=["bytes", "repetitions","time","MBps"] )
imb_scrittura_home = pd.read_csv("./dat-file/IMB-IO-S_Write-indv.dat",comment="#", sep='\s+',  names=["bytes", "repetitions","time","MBps"] )

imb_lettura_scratch = pd.read_csv("./dat-file/IMB-IO-S_Read-indv.SCRATCH.dat",comment="#", sep='\s+',  names=["bytes", "repetitions","time","MBps"] )
imb_scrittura_scratch = pd.read_csv("./dat-file/IMB-IO-S_Write-indv.SCRATCH.dat",comment="#", sep='\s+',  names=["bytes", "repetitions","time","MBps"] )

# Confronto della banda (Mbyes/s) tra SHM, OPA e IB al crescere della dimensione dei messaggi 
plt.title('Confronto velocità scrittura/lettura (Mbyes/s) tra Home e SCRATCH')
plt.grid()
plt.xlabel('Grandezza messaggio in bytes')
plt.ylabel('(Mbyes/s)')
plt.xscale('log')

plt.plot(imb_lettura_home.bytes,imb_lettura_home.MBps,'ro',label='Lettura Home', linewidth=2, linestyle='-')
plt.plot(imb_scrittura_home.bytes,imb_scrittura_home.MBps,'bo',label='Scrittura Home', linewidth=2, linestyle='-')

plt.plot(imb_lettura_scratch.bytes,imb_lettura_scratch.MBps,'go',label='Lettura SCRATCH', linewidth=2, linestyle='-')
plt.plot(imb_scrittura_scratch.bytes,imb_scrittura_scratch.MBps,'yo',label='Scrittura SCRATCH', linewidth=2, linestyle='-')


plt.legend(shadow=True)
plt.savefig('./output-plot/confronto-lettura-scrittura-home-SCRATCH.png')



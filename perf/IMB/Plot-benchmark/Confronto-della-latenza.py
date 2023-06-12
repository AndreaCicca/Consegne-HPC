import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import pandas as pd 

imb_infi = pd.read_csv("./dat-file/IMB-MPI1.infiniband.dat",comment="#", sep='\s+',  names=["bytes", "repetitions","time","MBps"] )
imb_opa = pd.read_csv("./dat-file/IMB-MPI1.opa.dat",comment="#", sep='\s+',  names=["bytes", "repetitions","time","MBps"] )
imb_shm = pd.read_csv("./dat-file/IMB-MPI1.shm.dat",comment="#", sep='\s+',  names=["bytes", "repetitions","time","MBps"] )

# Confronto della banda (Mbyes/s) tra SHM, OPA e IB al crescere della dimensione dei messaggi 
plt.title('Confronto della latenza tempo in us')
plt.grid()
plt.xlabel('Grandezza del messaggio in bytes')
plt.ylabel('Latenza del messaggio in us')

plt.plot(imb_infi.bytes,imb_infi.time,'ro',label='Infiniband', linewidth=2, linestyle='-')
plt.plot(imb_opa.bytes,imb_opa.time,'bo',label='Opa', linewidth=2, linestyle='-')
plt.plot(imb_shm.bytes,imb_shm.time,'go',label='Shm', linewidth=2, linestyle='-')

plt.legend(shadow=True)
plt.savefig('./output-plot/confronto-latenza.png')


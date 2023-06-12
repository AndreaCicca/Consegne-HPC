import matplotlib
matplotlib.use('Agg')   # Backend per PNG (http://matplotlib.org/faq/usage_faq.html#what-is-a-backend )
import matplotlib.pyplot as plt
import info_personali as ip
import pandas as pd

df_blocksize = pd.read_csv('blocksize.csv', sep=',', header=None, names=['time'])

lista_blocksize = [4, 8, 16, 32]

df_blocksize['time'] = df_blocksize['time'].str.replace("TIME= ", '')

# converti in float 
df_blocksize['time'] = df_blocksize['time'].astype(float)

# plot
fig = plt.figure() #
top = fig.add_subplot(111) # 1 riga, 1 colonna, figura 1
top.set_title(' Confronto blocksize ' + ip.get_user() + ' ' + ip.get_timestamp())
top.grid(True)
top.plot(lista_blocksize, df_blocksize["time"]/1000, 'r', label='blocksize')
top.set_xlabel('blocksize')
top.set_ylabel('Tempo (s)')
top.legend(loc='upper left')

plt.savefig('confronto-blocksize.png')

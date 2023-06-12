import matplotlib
matplotlib.use('Agg')   # Backend per PNG (http://matplotlib.org/faq/usage_faq.html#what-is-a-backend )
import matplotlib.pyplot as plt
import info_personali as ip
import pandas as pd

df_cudaEvent = pd.read_csv('cudaEvent.csv', sep=',', header=None, names=['matrix-size', 'time'])
df_gettimeofday = pd.read_csv('gettimeofday.csv', sep=',', header=None, names=['matrix-size', 'time'])


df_cudaEvent['time'] = df_cudaEvent['time'].str.replace("TIME= ", '')
df_gettimeofday['time'] = df_gettimeofday['time'].str.replace("TIME= ", '')

# print(df_cudaEvent)
# print(df_gettimeofday)

df_cudaEvent['time'] = df_cudaEvent['time'].astype(float)
df_gettimeofday['time'] = df_gettimeofday['time'].astype(float)

# plotto i 2 grafici

fig = plt.figure() #
top = fig.add_subplot(111) # 1 riga, 1 colonna, figura 1
top.set_title(' Confronto CudaEvents e gettimeofday ' + ip.get_user() + ' ' + ip.get_timestamp())
top.grid(True)
top.plot(df_cudaEvent["matrix-size"], df_cudaEvent["time"]/1000, 'r', label='CudaEvents')
top.plot(df_gettimeofday["matrix-size"], df_gettimeofday["time"], 'b', label='gettimeofday')
top.set_xlabel('Grandezza matrice')
top.set_ylabel('Tempo (s)')
top.legend(loc='upper left')


plt.savefig('confronto-cudaEvents-gettimeofday.png')

plt.yscale('log')

plt.savefig('confronto-cudaEvents-gettimeofday_log.png')
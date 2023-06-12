import matplotlib
matplotlib.use('Agg')   # Backend per PNG (http://matplotlib.org/faq/usage_faq.html#what-is-a-backend )
import matplotlib.pyplot as plt
import info_personali as ip
import pandas as pd

df_naive_cpu = pd.read_csv('Naive-CPU.txt', sep='\s+', header=None, names=['Processing time', 'GFLOPS'])
df_naive_gpu = pd.read_csv('Naive-GPU.txt', sep='\s+', header=None, names=['Processing time', 'GFLOPS'])
df_tiling = pd.read_csv('tiling.txt', sep='\s+', header=None, names=['Processing time', 'GFLOPS'])
df_coalescing = pd.read_csv('coalescing-GPU.txt', sep='\s+', header=None, names=['Processing time', 'GFLOPS'])

start = 100
end = 4000
increment = 200

sequence = list(range(start, end, increment))

# print(sequence)

fig = plt.figure() # 
top = fig.add_subplot(111) # 1 riga, 1 colonna, figura 1
top.set_title(' Matrix GFLOPS scaling ' + ip.get_user() + ' ' + ip.get_timestamp())
top.grid(True)
top.plot(sequence, df_naive_cpu["GFLOPS"], 'r', label='Naive CPU')
top.plot(sequence, df_naive_gpu["GFLOPS"], 'b', label='Naive GPU')
top.plot(sequence, df_tiling["GFLOPS"], 'g', label='Tiling')
top.plot(sequence, df_coalescing["GFLOPS"], 'y', label='Coalescing')
top.set_xlabel('Grandezza matrice')
top.set_ylabel('GFLOPS')
top.legend(loc='upper left')

plt.savefig('GPU-scaling-comparazione.png')

plt.clf()

fig = plt.figure()

botton = fig.add_subplot(111) # 1 riga, 1 colonna, figura 1
botton.set_title("Matrix processing time scaling")
botton.grid(True)
#botton.plot(sequence, df_naive_cpu["Processing time"], 'r', label='Naive CPU')
botton.plot(sequence, df_naive_gpu["Processing time"], 'b', label='Naive GPU')
botton.plot(sequence, df_tiling["Processing time"], 'g', label='Tiling')
botton.plot(sequence, df_coalescing["Processing time"], 'y', label='Coalescing')
botton.set_xlabel('Grandezza matrice')
botton.set_ylabel('Processing time')
botton.legend(loc='upper right')


plt.savefig('GPU-scaling-comparazione-time.png')

#plt.show()

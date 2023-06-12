#https://www.easytweaks.com/bar-plot-python-pandas-dataframe-example/
import info_personali as ip
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv("disktest.csv",comment="#", sep='\s+')
#print df

plt.suptitle('Disktest tra Home e Scratch ' + ip.get_user() + ' ' + ip.get_timestamp())

df.plot(kind='bar',  x='device');

plt.ylabel('MB/s')
plt.savefig('disktest_barplot.png')

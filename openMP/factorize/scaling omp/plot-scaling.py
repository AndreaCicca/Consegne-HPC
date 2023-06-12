import pandas as pd
import matplotlib.pyplot as plt

df_72 = pd.read_csv("omp-scaling-72bit.csv", names=["core", "module", "time"], sep=" ")
df_64 = pd.read_csv("omp-scaling-64bit.csv", names=["core", "module", "time"], sep=" ")


plt.figure()
plt.plot(df_72["core"], df_72["time"], label="72 bit")
plt.plot(df_64["core"], df_64["time"], label="64 bit")

plt.legend()
plt.grid()
plt.xlabel("core")
plt.ylabel("time")
plt.savefig("omp-scaling.png")

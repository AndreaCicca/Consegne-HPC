import pandas as pd
import matplotlib.pyplot as plt

pd_4 = pd.read_csv("output/csv/output_4.csv", sep=",", names=["matrix-size", "time"])
pd_8 = pd.read_csv("output/csv/output_8.csv", sep=",", names=["matrix-size", "time"])
pd_16 = pd.read_csv("output/csv/output_16.csv", sep=",", names=["matrix-size", "time"])
pd_32 = pd.read_csv("output/csv/output_32.csv", sep=",", names=["matrix-size", "time"])

plt.figure()

# fammi i plot con linee e punti

plt.plot(pd_4["matrix-size"], pd_4["time"], 'r', label="4 x 4 block size")
plt.plot(pd_8["matrix-size"], pd_8["time"], 'b', label="8 x 8 block size")
plt.plot(pd_16["matrix-size"], pd_16["time"], 'g', label="16 x 16 block size")
plt.plot(pd_32["matrix-size"], pd_32["time"], 'y', label="32 x 32 block size")

plt.grid(True)
plt.xlabel("Matrix size")
plt.ylabel("Time (s)")
plt.legend(loc='upper left')

plt.savefig("comparazione_size-block_matrix_size.png")
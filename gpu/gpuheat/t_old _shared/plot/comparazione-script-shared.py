import pandas as pd
import matplotlib.pyplot as plt

pd_shared = pd.read_csv("../csv/heat_shared.csv", sep=",", names=["matrix-size", "time"])
pd_standard = pd.read_csv("../csv/heat_standard.csv", sep=",", names=["matrix-size", "time"])


plt.figure()

# fammi i plot con linee e punti

plt.plot(pd_shared["matrix-size"], pd_shared["time"], 'r', label="Shared memory")
plt.plot(pd_standard["matrix-size"], pd_standard["time"], 'b', label="Standard memory")


plt.grid(True)
plt.xlabel("Matrix size")
plt.ylabel("Time (s)")
plt.legend(loc='upper left')

plt.savefig("comparazione-shared.png")
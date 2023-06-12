import pandas as pd
import matplotlib.pyplot as plt
# Numero blocchi, Errore stimato, Tempo di esecuzione, somma
df = pd.read_csv("output_scaling.csv", sep=",", header=0, names=["n_blocchi", "err", "time", "sum"])

# devo effettuare 2 flot nella stessa immagine, blocchi tempo e blocchi errore

# primo plot

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.errorbar(df["n_blocchi"], df["time"], yerr=df["err"], marker=".", color="red")
plt.xlabel("Numero blocchi")
plt.ylabel("Tempo di esecuzione")
plt.grid(True)
plt.title("Tempo di esecuzione in funzione del numero di blocchi")

# secondo plot
plt.subplot(2, 1, 2)
plt.errorbar(df["n_blocchi"], df["err"], marker=".", color="blue")
plt.xlabel("Numero blocchi")
plt.ylabel("Errore stimato")
plt.grid(True)
plt.title("Errore stimato in funzione del numero di blocchi")
plt.yscale("log")

plt.savefig("cpi2_scaling.png")
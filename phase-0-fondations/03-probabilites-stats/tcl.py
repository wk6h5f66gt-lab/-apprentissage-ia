import numpy as np
import matplotlib.pyplot as plt

n = 100_000
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, nb_des in zip(axes, [1, 2, 10]):
    lancers = np.random.randint(1, 7, size=(n, nb_des))
    sommes = lancers.sum(axis=1)
    ax.hist(sommes, bins=range(nb_des, 6 * nb_des + 2), density=True, edgecolor="black")
    ax.set_title(f"Somme de {nb_des} dé(s)")

plt.savefig("phase-0-fondations/03-probabilites-stats/tcl.png")
print("Graphique enregistré")

notes = np.array([6, 8, 10, 12, 14, 200])
z = (notes - np.mean(notes)) / np.std(notes)
print(z)
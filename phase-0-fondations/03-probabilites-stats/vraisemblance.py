import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(0.01, 0.99, 99)                       # 99 valeurs de p : 0.01, 0.02, ..., 0.99
vraisemblance = p**7 * (1 - p)**3                     # pour les 99 valeurs à la fois
log_vraisemblance = 7 * np.log(p) + 3 * np.log(1 - p)

print(f"Maximum de L     en p = {p[np.argmax(vraisemblance)]:.2f}")
print(f"Maximum de log L en p = {p[np.argmax(log_vraisemblance)]:.2f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(p, vraisemblance)
axes[0].set_title("Vraisemblance L(p)")
axes[1].plot(p, log_vraisemblance)
axes[1].set_title("Log-vraisemblance log L(p)")
for ax in axes:
    ax.set_xlabel("p")
plt.savefig("phase-0-fondations/03-probabilites-stats/vraisemblance.png")

# Le problème numérique
probas = np.full(1000, 0.01)          # 1000 fois la valeur 0.01
print(f"Produit des probabilités : {np.prod(probas)}")
print(f"Somme des logarithmes    : {np.sum(np.log(probas)):.2f}")
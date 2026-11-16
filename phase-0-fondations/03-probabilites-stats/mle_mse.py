import numpy as np

x = np.array([50, 80, 100])
y = np.array([150, 240, 310])
b = -10.5                                  # on fixe b pour ne chercher que w
w_candidats = np.linspace(2.5, 4, 151)     # 2.50, 2.51, ..., 4.00

mses = []
for w in w_candidats:
    y_pred = w * x + b
    mses.append(np.mean((y - y_pred) ** 2))
print(f"Meilleur w selon la MSE : {w_candidats[np.argmin(mses)]:.2f}")

for sigma in [2, 5, 20]:
    log_vraisemblances = []
    for w in w_candidats:
        y_pred = w * x + b
        log_L = -len(y) * np.log(sigma * np.sqrt(2 * np.pi)) - np.sum((y - y_pred) ** 2) / (2 * sigma**2)
        log_vraisemblances.append(log_L)
    print(f"σ = {sigma:>2} : meilleur w selon la vraisemblance : {w_candidats[np.argmax(log_vraisemblances)]:.2f}")
import numpy as np 

u= [2, 4, 4, 4, 5, 5, 7, 9]

def moyenne(u):
    sums=0
    for i in range(len(u)):
        sums+=u[i]
    return sums/len(u)
def varience(u) :
    m=moyenne(u)
    sums=0
    for i in range(len(u)):
        sums+=(u[i]-m)**2
    return sums/len(u)

v=np.array([2, 4, 4, 4, 5, 5, 7, 9])

moynump =np.mean(v)
varnump =np.var(v)

print(f"la moyenne de u avec python pur est : {moyenne(u)}")
print(f"la variance de u avec python pur est : {varience(u)}")

print(f"la moyenne de v avec numpy est : {moynump}")
print(f"la variance de v avec numpy est : {varnump}")

y = np.array([150, 240, 310])

meilleur_c = None
meilleure_mse = float("inf")

for k in range(30001):
    c = 100 + k / 100              
    mse = np.mean((c - y) ** 2)    
    if mse < meilleure_mse:
        meilleure_mse = mse
        meilleur_c = c

print(f"Meilleure constante : {meilleur_c:.2f}, MSE = {meilleure_mse:.2f}")
print(f"Moyenne : {np.mean(y):.2f}, variance : {np.var(y):.2f}")

x = np.array([[50], [80], [100]])
w = np.array([3.18])
b = -10.5

y_pred = x@w+b                   
mse_modele = np.mean((y_pred - y) ** 2)
r2 = 1 - mse_modele / np.var(y)

print(f"MSE du modèle : {mse_modele:.2f}")
print(f"R² = {r2:.4f}")
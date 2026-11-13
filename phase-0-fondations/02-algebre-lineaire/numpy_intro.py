import numpy as np 

u =np.array([1,-2,3])
v =np.array([4,0,2])
produit_scalaire=u@v
print(produit_scalaire)

q =np.array([3,4])
norme_q = np.linalg.norm(q)
print(norme_q)

x=np.array([[1,2],[3,0],[-1,4]])
w=np.array([2,-1])
b=np.array([1])
predire=x@w+b
print(predire)

j=np.array([[50],[80],[100]])
p=np.array([150,240,310])
W=np.array([3])
B=np.array([0])
mse = np.mean((j@W+B-p)**2)
print(mse)

import time

n = 1_000_000
u = np.random.rand(n)          # 1 million de nombres aléatoires
v = np.random.rand(n)

debut = time.perf_counter()    # on lance le chronomètre
total = 0
for i in range(n):
    total += u[i] * v[i]
temps_boucle = time.perf_counter() - debut

u @ v   # échauffement : ce premier appel n'est pas chronométré

debut = time.perf_counter()
for _ in range(100):
    resultat = u @ v
temps_numpy = (time.perf_counter() - debut) / 100

print(f"Boucle : {temps_boucle:.4f} s")
print(f"NumPy  : {temps_numpy:.6f} s")
print(f"NumPy est {temps_boucle / temps_numpy:.0f} fois plus rapide")
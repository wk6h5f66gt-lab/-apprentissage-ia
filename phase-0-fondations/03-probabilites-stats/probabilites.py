import numpy as np

for n in [10, 100, 10_000, 1_000_000]:
    lancers = np.random.randint(1, 7, size=n)   # n lancers de dé
    print(f"n = {n:>9} : moyenne = {np.mean(lancers):.4f}")

gains = np.random.choice([0, 10, 50], size=1_000_000, p=[0.5, 0.3, 0.2])
print(f"n = {len(gains):>9} : moyenne = {np.mean(gains):.4f}")
print(f"n = {len(gains):>9} : variance = {np.std(gains):.4f}") 

tailles = np.random.normal(175, 7, size=1_000_000)   # 1 million de tailles

dans_intervalle = (tailles >= 168) & (tailles <= 182)
print(f"Entre 168 et 182 : {np.mean(dans_intervalle):.4f}")

dans_intervalle1 = (tailles>=182)
print(f"Plus grand que 182 : {np.mean(dans_intervalle1):.4f}")

dans_intervalle2 = (tailles>=175)&(tailles<=189)
print(f"Entre 175 et 189 : {np.mean(dans_intervalle2):.4f}")

dans_intervalle3 = (tailles>=196)
print(f"Plus grand que 196 : {np.mean(dans_intervalle3):.4f}")
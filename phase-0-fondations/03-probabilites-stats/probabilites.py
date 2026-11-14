import numpy as np

for n in [10, 100, 10_000, 1_000_000]:
    lancers = np.random.randint(1, 7, size=n)   # n lancers de dé
    print(f"n = {n:>9} : moyenne = {np.mean(lancers):.4f}")

gains = np.random.choice([0, 10, 50], size=1_000_000, p=[0.5, 0.3, 0.2])
print(f"n = {len(gains):>9} : moyenne = {np.mean(gains):.4f}")
print(f"n = {len(gains):>9} : variance = {np.std(gains):.4f}") 
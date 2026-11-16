import numpy as np

x = np.array([50, 80, 100])
y = np.array([150, 240, 310])
b = -10.5

def perte(w):
    y_pred = w * x + b
    return np.mean((y - y_pred) ** 2)

def derivee_formule(w):
    y_pred = w * x + b
    return -2 / len(x) * np.sum(x * (y - y_pred))

def derivee_numerique(w, h=0.0001):
    return (perte(w + h) - perte(w - h)) / (2 * h)

for w in [3.0, 3.18, 3.5]:
    print(f"w = {w:.2f} | formule : {derivee_formule(w):10.2f} | numérique : {derivee_numerique(w):10.2f}")
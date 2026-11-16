import numpy as np

x = np.array([50, 80, 100])
y = np.array([150, 240, 310])

def perte(w, b):
    y_pred = w * x + b
    return np.mean((y - y_pred) ** 2)

def gradient(w, b):
    e = y - (w * x + b)                  # vecteur des erreurs
    dw = -2 / len(x) * (x @ e)           # ∂L/∂w
    db = -2 / len(x) * np.sum(e)         # ∂L/∂b
    return dw, db

def gradient_numerique(w, b, h=0.0001):
    dw = (perte(w + h, b) - perte(w - h, b)) / (2 * h)   # on ne bouge que w
    db = (perte(w, b + h) - perte(w, b - h)) / (2 * h)   # on ne bouge que b
    return dw, db

for w, b in [(3, 0), (3.18, -10.5), (2, 50)]:
    dw, db = gradient(w, b)
    dw_num, db_num = gradient_numerique(w, b)
    print(f"(w={w}, b={b}) | formule : ({dw:9.2f}, {db:7.2f}) | numérique : ({dw_num:9.2f}, {db_num:7.2f})")
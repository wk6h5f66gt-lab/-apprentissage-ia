def produit_scalaire(u, v):
    if len(u) != len(v):
        raise ValueError("Les vecteurs doivent avoir la même dimension.")
    total = 0
    for i in range(len(u)):
        total += u[i] * v[i]
    return total


def predire(X, w, b):
    predictions = []
    for ligne in X:                                  
        predictions.append(produit_scalaire(ligne, w) + b)
    return predictions


def mse_vectorielle(X, y, w, b):
    y_pred = predire(X, w, b)                         
    e = []
    for i in range(len(y)):
        e.append(y_pred[i] - y[i])                   
    return produit_scalaire(e, e) / len(y)            


if __name__ == "__main__":
    X = [[50], [80], [100]]
    y = [150, 240, 310]
    print(f"MSE (w=3, b=0) : {mse_vectorielle(X, y, [3], 0):.2f}")   

    # Exercice à la main : 3 lignes, 2 colonnes → forme (3, 2)
    X2 = [[1, 2], [3, 0], [-1, 4]]
    print(predire(X2, [2, -1], 1))                                  
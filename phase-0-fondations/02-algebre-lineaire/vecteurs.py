def produit_scalaire(u,v):
    if(len(u) ==len(v)):
        pscalaire=0
        for i in range(len(u)):
            pscalaire+=u[i]*v[i]
        return pscalaire
    else :
        raise ValueError("Les vecteurs doivent avoir la même dimension.")
def norme(v):
    return produit_scalaire(v, v) ** 0.5
x=[120,4,15]
w=[3,10,-0.5]
prix=produit_scalaire(x,w)+20
print(f"le prix de la maison est {prix}")
print(produit_scalaire([1, -2, 3], [4, 0, 2]))   # attendu : 10
print(norme([3, 4]))                              # attendu : 5.0
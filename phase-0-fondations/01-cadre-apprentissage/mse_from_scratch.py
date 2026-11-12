xs = [50,80,100]
ys=[150,240,310]
def prediction(x,w,b):
    return w*x+b
def mse(xs,ys,w,b):
    total=0
    for i in range(0,len(xs)):
     total=total+((prediction(xs[i],w,b)-ys[i]))**2
    return total/len(xs)

print(f"MSE du modèle A (w=3, b=0)    : {mse(xs, ys, 3, 0):.2f}")
print(f"MSE du modèle B (w=2.5, b=20) : {mse(xs, ys, 2.5, 20):.2f}")
meilleure_mse=mse(xs,ys,3,0)
meilleur_w=3
meilleur_b=0
for i in range(201):
   w=2+i/100
   for j in range(1001):
      b = -50 + j / 10
      erreur = mse(xs, ys, w, b)   
      if erreur < meilleure_mse:
         meilleur_w=w
         meilleur_b=b
         meilleure_mse=erreur
print(f"Meilleur modèle : w = {meilleur_w:.2f}, b = {meilleur_b:.1f}, MSE = {meilleure_mse:.2f}")      
  
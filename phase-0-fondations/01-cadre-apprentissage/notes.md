# Leçon 1 : qu'est-ce qu'apprendre pour une machine ?

> Apprendre, c'est chercher, dans une famille de fonctions, celle qui minimise une erreur mesurée sur des données.

## Programmation classique et Machine Learning
- **Programmation classique** : données + règles → réponses. C'est le développeur qui écrit les règles.
- **Machine Learning** : données + réponses → règles. C'est l'algorithme qui trouve le modèle.
- Hypothèse de départ : une fonction inconnue f* relie x à y. On construit une approximation f̂ à partir d'exemples.

## Vocabulaire
- **x** (features) : les entrées connues, souvent un vecteur.
- **y** (target ou label) : ce qu'on veut prédire.
- **Exemple** : un couple (x⁽ⁱ⁾, y⁽ⁱ⁾). Le (i) est le numéro de l'exemple, pas une puissance.
- **Dataset** : n exemples, rangés dans une matrice X de taille (n, d).

## Les 4 ingrédients
1. **Les données** : les exemples (x, y), fournis par l'humain.
2. **Le modèle** : une famille de fonctions paramétrées, par exemple f(x) = w·x + b. L'humain choisit la forme, la machine règle la valeur des paramètres.
3. **La fonction de perte** : un nombre qui mesure à quel point le modèle se trompe. Elle est choisie par l'humain et sert de boussole à l'apprentissage.
4. **L'optimisation** : la méthode qui ajuste les paramètres pour minimiser la perte.

Pendant l'apprentissage, les données ne changent jamais. Seuls les paramètres bougent, et la perte change en conséquence.

## Les types de problèmes
On se pose deux questions, dans cet ordre :
1. A-t-on les réponses y ? Si non, c'est du **non supervisé**. Si oui, c'est du supervisé.
2. Dans le supervisé : y est-il une quantité ou une catégorie ?

- **Régression** : y est une quantité continue. La question est « combien ? ». Exemples : le prix d'une maison, un âge.
- **Classification** : y est une catégorie, binaire ou multi-classe. La question est « laquelle ? ». Exemples : fraude ou normale, un chiffre manuscrit de 0 à 9.
- **Non supervisé** : il n'y a pas de y. On cherche une structure dans les données, par exemple avec le clustering de clients.

Le test pour trancher : si la distance et la moyenne entre deux valeurs de y ont un sens, c'est de la régression. Sinon, c'est de la classification. Attention, des chiffres peuvent n'être que des étiquettes.

## Les features
- Une feature est une variable qui prend une valeur pour chaque exemple.
- Une bonne feature varie d'un exemple à l'autre et influence y.
- Il en existe trois types : numérique (un montant), binaire (à l'étranger : oui ou non), catégorielle (le canal de paiement).
- Le **feature engineering** consiste à construire des features plus utiles, par exemple l'écart entre une transaction et les habitudes du client.

## La MSE (erreur quadratique moyenne)
- MSE = (1/n) × Σ (f(x⁽ⁱ⁾) − y⁽ⁱ⁾)²
- Le calcul : pour chaque exemple, on prédit, on calcule l'erreur et on la met au carré. On fait la somme, puis on divise par n.
- Pourquoi le carré :
  - les erreurs positives et négatives ne s'annulent pas ;
  - les grosses erreurs sont plus pénalisées ;
  - la fonction obtenue est lisse et dérivable.
- Conséquence : la MSE préfère plusieurs petites erreurs à une seule grosse.
- La MSE s'exprime en unité au carré (k€²). La RMSE = √MSE revient à l'unité d'origine.

## Généralisation et sur-apprentissage
- Le vrai but : bien prédire sur des données jamais vues.
- On sépare les données avant l'entraînement :
  - le **train** (environ 80 %) sert à entraîner le modèle ;
  - le **test** (environ 20 %) n'est jamais vu pendant l'entraînement.
- Le **risque empirique** se calcule sur nos données. Le **risque réel** porte sur toutes les données possibles et reste inconnu.
- Une erreur de 0 est suspecte : le modèle a peut-être mémorisé le bruit, ou il y a une fuite de données (*data leakage*).

| Erreur train | Erreur test | Diagnostic |
|---|---|---|
| Faible | Faible | Bon modèle, qui généralise |
| Faible | Élevée | Sur-apprentissage : le modèle a mémorisé |
| Élevée | Élevée | Sous-apprentissage : le modèle est trop simple |

## Ce que j'ai codé
- `mse_from_scratch.py`, en Python pur, avec deux fonctions : `prediction` et `mse`.
- Modèle A (w = 3, b = 0) : MSE = 33,33.
- Modèle B (w = 2,5, b = 20) : MSE = 675.
- Recherche par grille : meilleur modèle trouvé avec w = 3,18 et b = −10,5, pour une MSE de 7,90. L'optimum exact est d'environ 7,89.
- Limites de la recherche par grille :
  - elle ne trouve que le meilleur parmi les valeurs testées ;
  - son coût explose avec le nombre de paramètres. D'où le besoin de la descente de gradient.

## Mes erreurs à retenir
- Initialiser l'accumulateur (`total = 0`) **avant** la boucle.
- Ne pas appeler une variable `sum` : c'est le nom d'une fonction intégrée de Python.
- Écrire `2.5` et non `2,5` : la virgule sépare les arguments.
- `range(fin)` exclut la fin. Nombre de valeurs = (fin − début) / pas + 1, sinon c'est l'erreur *off-by-one*.
- La puissance s'écrit `**`, pas `^`.
- Indenter avec 4 espaces. Un `print` placé dans une boucle s'exécute à chaque tour.
- Ne pas recalculer deux fois la même chose : stocker le résultat dans une variable.
- Vérifier que l'espace de recherche couvre les bonnes valeurs.
- Dans les commandes, remplacer les exemples comme `<ton-pseudo>`, chevrons compris.

## Git et Linux
- La routine Git : `git status`, puis `git add`, puis `git commit -m "..."`, puis `git push`.
- Les commandes Linux : `pwd`, `ls -la`, `cd`, `mkdir`, `cp`, `mv`, `rm`. Attention, `rm` n'a pas de corbeille. La touche **Tab** complète les noms.
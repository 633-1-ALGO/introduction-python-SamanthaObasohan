# Problème : Etant donné deux variables c et d, on veut savoir si leur produit est négatif ou positif ou nul.
# Contrainte : Ne pas calculer le produit des deux nombres.
# Résultat attendu : Un message affichant "Produit positif" ou "Produit négatif" ou "Produit nul".
# Indications :  Vous pouvez changer les valeurs des variables pour vos tests.
c = 42
d = 31

if c>d :
    print("Produit positif")
if c<d :
    if c!=0:
        print("Produit négatif")
if c==0 :
    print("Produit null")
if d==0 :
    print("Produit null")
else:
    print("Produit :",c*d)

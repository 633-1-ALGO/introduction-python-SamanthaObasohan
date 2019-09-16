# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

compteur = 0
for nombre in B:
    while compteur<len(B):
        compteur = compteur+1
        element1 = B[compteur]
        element2 = B[compteur+1]
        if element1 > element2:
            B[compteur+1] = element1
            B[compteur] = element2



print("Le tableau B trié : ",B)

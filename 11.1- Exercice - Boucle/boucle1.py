# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A
A = [1, 5, 15, 25, 10, 55, 50, 35]
somme = 0

for nombre in A:
    somme = nombre + somme

moyenne = somme/len(A)

print("Moyenne = ",moyenne)

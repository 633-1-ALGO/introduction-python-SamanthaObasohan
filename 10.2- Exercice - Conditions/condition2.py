# Problème : Déterminer si une année est bissextile ou non. Pour cela, il faut avoir ces règles en tête :
#                   Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
#                   Si elle est multiple de 4, on regarde si elle est multiple de 100.
#                       Si c'est le cas, on regarde si elle est multiple de 400.
#                           Si c'est le cas, l'année est bissextile.
#                           Sinon, elle n'est pas bissextile.
#                       Sinon, elle est bissextile.
#
# Résultat attendu : Un message affichant "Année bissextile" ou "Année non bissextile"

annee = 2019
multiple100 = (annee*4)/100
multiple400 = (annee*4)/400
multiple4 = annee/4

if multiple4.is_integer():
    if multiple100.is_integer():
        if multiple400.is_integer():
            print('Année ',annee,' biesxtile')
        else :
            print('Année ',annee,' non biesxtile')
    print('Année ',annee,' biesxtile')
else:
    print('Année ',annee,' non biesxtile')

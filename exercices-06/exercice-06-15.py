# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15


chaine_plus_longue = ""


for i in enumerate(my_list):
    if chaine_plus_longue > len(my_list):
        i += chaine_plus_longue
        
print(chaine_plus_longue)

# je n'y arrive pas
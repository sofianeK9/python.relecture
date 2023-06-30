# exo 3.2
# Bob veut distribuer tous ses bonbons et chocolats à ses amis.
# Il a 15 bonbons, 17 chocolats et 3 amis.
# Combien de bonbons lui restera-t-il ?
# Calculez le reste de bonbons puis stockez le résultat dans la variable `candies_rest`.
# Combien de chocolats lui restera-t-il ?
# Calculez le reste de chocolats puis stockez le résultat dans la variable `chocolates_rest`.
# Affichez ces résultats.

candies = 15
chocolates = 17
friends = 3

# réponse 3.2
candies_rest = candies / friends 
print(f"le reste de bonbons est de {candies_rest}")
# il ne lui restera aucun bonbon car ses 3 amis en auront eu 5
chocolates_rest = chocolates / friends
print(f"le reste de chocolat est de {round(chocolates_rest,0)}")
#similaire au cas ci-dessus




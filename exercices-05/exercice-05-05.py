# exo 5.5
# Trouvez au moins une façon de compter le nombre de lignes de la chaîne de caractère suivante :

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

# réponse 5.5
print(my_text.count(".") + 1)
#ou
print(my_text.count("\n") + 1)
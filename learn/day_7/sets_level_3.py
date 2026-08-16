age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 3

# Convertissez les âges en un ensemble et comparez la longueur de la liste et celle de l'ensemble. Laquelle est plus grande ?
set_age = set(age)
print(age, set_age)
# La liste est plus longue que l'ensemble

# Expliquez la différence entre les types de données suivants : chaîne, liste, tuple et ensemble
# Une chaine permet de sauvegarder une suite de caractère alphanumérique.
# Une liste est un ensemble ordonné et muable d'élements et peut contenir autant de donnée que la mémoire peut en supporter.
# Tuple est un ensemble ordonné immuable d'éléments et peut contenir autant de donnée que la mémoire peut en supporter. La seule différence avec une liste est qu'on ne peut pas directement modifier les données dans cette dernière après sa déclaration.

# I am a teacher and I love to inspire and teach people. Combien de mots uniques ont été utilisés dans cette phrase ? Utilisez les méthodes split et set pour obtenir les mots uniques.
phrase = "I am a teacher and I love to inspire and teach people"
phrase_to_list = phrase.split(" ")
phrase_to_set = set(phrase_to_list)
print(phrase_to_list, phrase_to_set)
print(f"Nombre de mot unique utilisés : {len(phrase_to_set)}")
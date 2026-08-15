# Level 1

# Créez un tuple vide.
my_tuple = ()

# Créez un tuple contenant les prénoms de vos sœurs et de vos frères (les frères et sœurs imaginaires sont acceptés).
brothers = ("John", "Tom", "Peter")
sisters = ("Nina", "Joe")

# Joignez les tuples frères et sœurs et assignez-les à siblings.
siblings = brothers + sisters
print(siblings)

# Combien de frères et sœurs avez-vous ?
print(f"J'ai {len(siblings)} frères et soeurs.")

# Modifiez le tuple siblings en ajoutant le prénom de votre père et de votre mère, puis assignez-le à family_members.
family_members = siblings + ("Tim", "Maeva")
print(family_members)

# Level 2

# Dépaquetez siblings et parents à partir de family_members.
*siblings, father, mother = family_members
print(f"Siblings = {siblings}")
print(f"Father = {father}")
print(f"Mother = {mother}")

# Créez des tuples fruits, légumes et produits animaux. Joignez les trois tuples et assignez-les à une variable appelée food_stuff_tp.
fruits = ("Pomme", "Mangue", "Orange", "Citron", "Fraise", "Kiwi", "Raisin", "Banane")
vegetables = ("Tomate", "Poivron", "Carotte", "Brocoli", "Aubergine", "Oignon", "Courgette")
animal_products = ("Viande", "Oeuf", "Poisson", "Lait", "Fromage", "Poulet")
food_stuff_tp = fruits + vegetables + animal_products

# Convertissez le tuple food_stuff_tp en une liste food_stuff_lt.
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Découpez l'élément ou les éléments du milieu du tuple food_stuff_tp ou de la liste food_stuff_lt.
print(food_stuff_lt[len(food_stuff_lt) // 2])

# Découpez les trois premiers et les trois derniers éléments de la liste food_stuff_lt.
print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

# Supprimez complètement le tuple food_stuff_tp.
del food_stuff_tp

# Vérifiez si un élément existe dans le tuple :
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Vérifiez si 'Estonia' est un pays nordique.
print("Estonia est un pays nordique ?", "Estonia" in nordic_countries)

# Vérifiez si 'Iceland' est un pays nordique.
print("Iceland est un pays nordique ?", "Iceland" in nordic_countries)






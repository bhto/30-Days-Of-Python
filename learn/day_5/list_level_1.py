# Déclarez une liste vide.
empty_list = []

# Déclarez une liste avec plus de 5 éléments.
my_list = ['Banane', 'Orange', 'Citron', 'Mangue', 'Mandarine', 'Noisette']

# Trouvez la longueur de votre liste.
print("Longueur de ma liste", len(my_list))

# Obtenez le premier élément, l'élément du milieu et le dernier élément de la liste.

print(my_list[0], my_list[(len(my_list) - 1) // 2], my_list[-1])

# Déclarez une liste appelée mixed_data_types contenant (votre nom, âge, taille, situation matrimoniale, adresse).

mixed_data_types = ["Bérenger", 150, '1m80', 'Couplibataire', '200 Rue de ta Maiiirrre']

# Déclarez une variable liste nommée it_companies et assignez-lui les valeurs initiales Facebook, Google, Microsoft, Apple, IBM, Oracle et Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Affichez la liste en utilisant print().
print(it_companies)

# Affichez le nombre d'entreprises dans la liste.
print(len(it_companies))

# Affichez la première, celle du milieu et la dernière entreprise.
print(it_companies[0], it_companies[(len(it_companies) - 1) // 2], it_companies[-1])

# Affichez la liste après avoir modifié l'une des entreprises.
it_companies[0] = 'Meta'
print(it_companies)

# Ajoutez une entreprise IT à it_companies
it_companies.append("Alibaba")

# Insérez une entreprise IT au milieu de la liste.
it_companies.insert((len(it_companies) - 1) // 2, "OpenAI")

# Changez l'un des noms de it_companies en majuscules (IBM exclu !).
it_companies[2] = it_companies[2].upper()
print(it_companies)

# Joignez les it_companies avec une chaîne '#'.
print('#'.join(it_companies))

# Vérifiez si une certaine entreprise existe dans la liste it_companies.
print("Amazon est elle dans la liste ?", "Amazon" in it_companies)

# Triez la liste avec la méthode sort().
it_companies.sort()

# Inversez la liste dans l'ordre décroissant avec la méthode reverse().
it_companies.reverse()

# Découpez les 3 premières entreprises de la liste.
print(it_companies[0:3])

# Découpez les 3 dernières entreprises de la liste.
print(it_companies[-3:])

# Supprimez la première entreprise IT de la liste.
del it_companies[0]

# Supprimez l'entreprise du milieu (ou les entreprises du milieu) de la liste.
del it_companies[(len(it_companies) - 1) // 2]

# Supprimez la dernière entreprise IT de la liste.
it_companies.remove("Amazon")

# Supprimez toutes les entreprises IT de la liste.
it_companies.clear()

# Détruisez la liste des entreprises IT.
del it_companies

# Joignez les listes suivantes :

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

technos = front_end + back_end

# Après avoir joint les listes à la question 26, copiez la liste jointe et assignez-la à une variable full_stack, puis insérez Python et SQL après Redux.

full_stack = technos.copy()
full_stack.extend(["Python", "SQL"])
full_stack.append("Redux")
print(full_stack)



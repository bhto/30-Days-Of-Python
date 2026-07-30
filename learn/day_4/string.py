# Concaténez les chaînes 'Thirty', 'Days', 'Of', 'Python' en une seule chaîne, 'Thirty Days Of Python'.
print('Thirty ' + 'Days ' + 'Of ' + 'Python')

# Concaténez les chaînes 'Coding', 'For', 'All' en une seule chaîne, 'Coding For All'.
print('Coding ', 'For ', 'All')

# Déclarez une variable nommée company et assignez-lui la valeur initiale "Coding For All"
company = "Coding For All"

# Affichez la variable company en utilisant print().
print(company)

# Affichez la longueur de la chaîne company avec len() et print().
print(len(company))

# Convertissez tous les caractères en majuscules avec upper().
print(company.upper())

# Convertissez tous les caractères en minuscules avec lower().
print(company.lower())

# Utilisez les méthodes capitalize(), title(), swapcase() pour formater la valeur 
# de la chaîne Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Découpez (slicez) le premier mot de la chaîne Coding For All.
print(company[0:6])

# Vérifiez si la chaîne Coding For All contient le mot Coding en 
# utilisant index(), find() ou d'autres méthodes.
print(f"Est ce que Coding est contenu dans {company} ?", "Coding" in company)

# Remplacez le mot coding dans la chaîne 'Coding For All' par Python.
print(company.replace("Coding", "Python"))

# Changez "Python for Everyone" en "Python for All" avec la 
# méthode replace() ou une autre méthode.
chaine = "Python for Everyone"
print(chaine.replace("Python for Everyone", "Python for All"))

# Découpez la chaîne 'Coding For All' en utilisant l'espace comme séparateur (split()).
print(company.split(' '))

# Découpez la chaîne "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" au niveau de la virgule.
chaine = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(chaine.split(", "))

# Quel est le caractère à l'indice 0 dans la chaîne Coding For All ?
print(f"Caractère à l'indice 0 dans {company} est: {company[0]}")

# Quel est le dernier indice de la chaîne Coding For All ?
print(f"Le dernier indice de la chaine {company} est {len(company) - 1}")

# Quel caractère se trouve à l'indice 10 dans la chaîne "Coding For All" ?
print(f"Caractère à l'indice 10 dans {company} est: {company[10]}")

# Créez un acronyme ou une abréviation pour le nom 'Python For Everyone'
nom = "Python For Everyone"
abreviation = nom.split(' ')[0]
print(f"L'abréviation de {nom} est {abreviation}")

# Créez un acronyme ou une abréviation pour le nom 'Coding For All'.
nom = 'Coding For All'
abreviation = nom.split(' ')[0]
print(f"L'abréviation de {nom} est {abreviation}")

# Utilisez index() pour déterminer la position de la première occurrence de C dans Coding For All.
print(f"Index de la première occurence de C dans {company}: {company.index('C')}")

# Utilisez index() pour déterminer la position de la première occurrence de F dans Coding For All.
print(f"Index de la première occurence de F dans {company}: {company.index('F')}")

# Utilisez rfind() pour déterminer la position de la dernière occurrence de l dans Coding For All People.
print(f"Position de la dernière occurence de l dans {company} : {company.rfind('l')}")

# Utilisez index() ou find() pour trouver la position de la première occurrence du mot 'because' dans la phrase : 'You cannot end a sentence with because because because is a conjunction'
phrase = 'You cannot end a sentence with because because because is a conjunction'
print(phrase.find('because'))

# Utilisez rindex() pour trouver la position de la dernière occurrence du mot because dans la phrase : 'You cannot end a sentence with because because because is a conjunction'.
phrase = 'You cannot end a sentence with because because because is a conjunction'
print(phrase.rfind('because'))

# Extrayez (slicez) l'expression 'because because because' de la phrase : 'You cannot end a sentence with because because because is a conjunction'.
phrase = 'You cannot end a sentence with because because because is a conjunction'
print(phrase.replace('because because because', ''))

# Trouvez la position de la première occurrence du mot 'because' dans la phrase : 'You cannot end a sentence with because because because is a conjunction'
phrase = 'You cannot end a sentence with because because because is a conjunction'
print(f"Position du premier occurence de because : {phrase.find('because')}")

# Est-ce que 'Coding For All' commence par la sous-chaîne Coding ?
print(company.startswith('Coding'))

# Est-ce que 'Coding For All' se termine par la sous-chaîne coding ?
print(company.endswith('Coding'))

# '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;', supprimez les espaces de début et de fin dans la chaîne donnée.
sentence = '  Coding For All    '
print(sentence.strip())

# Parmi les variables suivantes, lesquelles renvoient True avec la méthode isidentifier() ?
# 30DaysOfPython
# thirty_days_of_python
print("30DaysOfPython => False")
print("thirty_days_of_python => True")

# La liste suivante contient les noms de certaines bibliothèques Python : ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Joignez la liste avec un dièse suivi d'un espace.
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(libs))

# Utilisez la séquence d'échappement de nouvelle ligne pour séparer les phrases suivantes :
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge. \nI just wonder what is next.')

# Utilisez la séquence d'échappement de tabulation pour écrire les lignes suivantes :
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name \t\tAge\t\t Country \t City")
print("Bérenger\t300\t\t Bénin\t\t Cotonou")

# Utilisez la méthode de formatage de chaînes pour afficher ce qui suit :
# The area of a circle with radius 10 is 314 meters square.
sentence = "The area of a circle with radius {} is {:.0f} meters square."
radius = 10
area = 3.14 * radius ** 2
print(sentence.format(radius, area))

# Réalisez ce qui suit en utilisant les méthodes de formatage de chaînes :

print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")
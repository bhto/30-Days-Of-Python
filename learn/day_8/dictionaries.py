# Créez un dictionnaire vide appelé dog
dog = {}

# Ajoutez les clés name, color, breed, legs, age au dictionnaire dog
dog['name'] = "Dog Name"
dog['color'] = "Dog color"
dog['breed'] = "Dog breed"
dog['legs'] = "Dog legs"
dog['age'] = "Dog age"
print(dog)

# Créez un dictionnaire student et ajoutez first_name, last_name, gender, age, marital status, skills, country, city et address comme clés du dictionnaire
student = {
    "first_name": "Doe",
    "last_name": "John",
    "gender": "Male",
    "age": 18,
    "marital_status": "Married",
    "skills": ["HTML", "JS", "PHP", "Python"],
    "country": "France",
    "city": "Lille",
    "address": {
        "street": "Space street",
        "zipcode": "02210"
    } 
}

# Obtenez la longueur du dictionnaire student
print(f"Longueur du dict student: {len(student)}")

# Obtenez la valeur de skills et vérifiez le type de données, il devrait s'agir d'une liste
print(f"Type de skills {type(student["skills"])}")

# Modifiez les valeurs de skills en ajoutant une ou deux compétences
student["skills"].extend(["TS", "C++"])
print(student)

# Obtenez les clés du dictionnaire sous forme de liste
print(student.keys())

# Obtenez les valeurs du dictionnaire sous forme de liste
print(student.values())

# Convertissez le dictionnaire en une liste de tuples avec la méthode items()
print(student.items())

# Supprimez l'un des éléments du dictionnaire
del student["marital_status"]
print(student)
# Supprimez l'un des dictionnaires
del student
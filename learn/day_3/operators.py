age = 19
size = 1.83
complex_number = 1j

base = float(input("Entrez la base : "))
height = float(input("Entrez la hauteur : "))
print("L'aire du triangle est", (base * height) / 2)

a = float(input("Entrez le côté a : "))
b = float(input("Entrez le côté b : "))
c = float(input("Entrez le côté c : "))
print("Le périmètre du triangle est ", a + b + c)

length = float(input("Longueur : "))
width = float(input("Largeur : "))

print("Aire du rectangle", length * width)
print("Périmètre du rectange", (length + width) * 2)

r = float(input("Rayon du cercle : "))
print("Aire du cercle", 3.14 * r ** 2)
print("Circonférence du cercle", 2 * 3.14 * r)

# Saut de 8 à 12
print("len(python) != len(dragon)", len("python") != len("dragon"))

print('<on> est dans python et dragon ?', 'on' in 'python' and 'on' in 'dragon')
print('Jargon est dans la phrase : I hope this course is not full of jargon ?', 'jargon' in 'I hope this course is not full of jargon')
print("'on' n'est pas dans python et dragon ?", 'on' not in 'python' and 'on' not in 'dragon')
print(str(float(len("python"))))

print("Un nombre est pair si le reste de sa division par 2 donne 0")
print("Vérifiez si la division entière de 7 par 3 est égale à la valeur convertie en entier de 2,7.", 7 // 3 == int(2.7))
print("Vérifiez si le type de '10' est égal au type de 10.", type('10') == type(10))

print("Vérifiez si int('9.8') est égal à 10.", float('9.8') == 10)

hours = int(input("Entrez les heures : "))
hourly_rate = int(input("Entez le taux horaire : "))

print("Votre salaire hedbomadaire est", hours * hourly_rate)

# Saut de 22

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)


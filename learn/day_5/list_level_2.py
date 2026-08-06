# Voici une liste de 10 âges d'étudiants :
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Triez la liste et trouvez l'âge minimum et maximum.
ages.sort()
print("Age min", ages[0], "Age max", ages[-1])

# Ajoutez à nouveau l'âge minimum et l'âge maximum à la liste.
ages.extend([ages[0], ages[-1]])

# Trouvez l'âge médian (un élément du milieu ou deux éléments du milieu divisés par deux).
print("Age médian", ages[(len(ages) - 1) // 2] // 2)

# Trouvez l'âge moyen (somme de tous les éléments divisée par leur nombre).
moyenne = sum(ages) / len(ages)
print("Age moyen", moyenne)

# Trouvez l'étendue des âges (max moins min).
print("Etendu des ages", max(ages) - min(ages))

# Comparez la valeur de (min - moyenne) et (max - moyenne), en utilisant abs().

val_min = abs(min(ages) - moyenne)
val_max = abs(max(ages) - moyenne)

print(val_min != val_max)

# Trouvez le(s) pays du milieu dans la liste des pays.
country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(country[len(country) // 2])

# Dépaquetez les trois premiers pays et le reste comme pays scandinaves.
china, russia, usa, *scandinaves = country
print(china, russia, usa, scandinaves)




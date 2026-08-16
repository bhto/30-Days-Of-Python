A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Level 2

# Joignez A et B
print(A.union(B))

# Trouvez l'intersection de A et B
print(A.intersection(B))

# A est-il un sous-ensemble de B
print("A est-il un sous-ensemble de B", A.issubset(B))

# A et B sont-ils des ensembles disjoints
print("A et B sont-ils des ensembles disjoints", A.isdisjoint(B))

# Joignez A avec B et B avec A
print(f"A | B = {A | B}")
print(f"B | A = {B | A}")

# Quelle est la différence symétrique entre A et B
print("Différence symétrique entre A et B", A.symmetric_difference(B))

# Supprimez complètement les ensembles
del A, B
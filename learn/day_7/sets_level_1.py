it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Level 1

# Trouvez la longueur de l'ensemble it_companies
print(f"Longueur de l'ensemble it_companies: {len(it_companies)}")

# Ajoutez 'Twitter' à it_companies
it_companies.add("Twitter")
print(it_companies)

# Insérez plusieurs entreprises informatiques à la fois dans l'ensemble it_companies
it_companies.update(["DELL", "HP", "OpenAI", "Anthropic"])
print(it_companies)

# Supprimez l'une des entreprises de l'ensemble it_companies
delete_companie = it_companies.remove("Microsoft")
print(it_companies)

# Quelle est la différence entre remove et discard
# Remove renvoie une erreur quand l'élément à supprimer n'existe pas dans l'ensemble.
# Par contre, discard ne renvoie pas d'erreur quand l'élément est inexistant.


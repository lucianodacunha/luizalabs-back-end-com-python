"""
Conhecendo a classe str
"""

# métodos úteis

pais = "Brazil"

print(pais.lower())
print(pais.upper())
print(pais.title())
print(pais.capitalize())
print(pais.center(20, "*"))
print("|".join(pais))
print(pais.replace("z", "s"))
pais = " " + pais + " "
print(pais)
print(pais.strip())
print(pais.rstrip())
print(pais.lstrip())
pais = pais.strip()
print(pais.startswith("B"))
print(pais.startswith("A"))
print(pais.endswith("l"))
print(pais.endswith("u"))
print(pais.find("r"))
print(pais.count("a"))
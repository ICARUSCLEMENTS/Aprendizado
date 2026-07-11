nome = "Ícaro"
sobrenome = "Clemente"
nome_completo = nome + " " + sobrenome

print("Nome completo (1ª forma):", nome_completo)
print("Nome completo (2ª forma):" + nome_completo)

print("Nome completo (3ª forma):" + nome + sobrenome)
print("Nome completo (4ª forma):" + nome + " " + sobrenome)
print("Nome completo (5ª forma):" + nome, sobrenome )

print("Nome completo (6ª forma): %s" % nome_completo)
print("Nome completo (7ª forma): %s %s" % (nome, sobrenome))

print(f"Nome completo (8ª forma): {nome} {sobrenome}")
print("Nome completo (9ª forma): {} {}".format(sobrenome, nome))

print(nome_completo.upper())
print(nome_completo.lower())
print(nome_completo.title())
print(nome_completo.capitalize())

print(nome_completo.split("a"))
print("xÍcaro Clementex".strip("x"))
print(nome_completo.replace("a", "o"))

print("(11) 99999-9999".replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))

print(nome_completo.count("e"))
print(nome_completo.find("a"))

print("-".join(nome_completo))
print(nome_completo.startswith("Í"))
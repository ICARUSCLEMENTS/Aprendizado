# Questão 1
nome = "Ícaro"
sobrenome = "Clemente"
nome_completo = nome + " " + sobrenome

print("1ª forma:", nome_completo)
print("2ª forma:" + nome_completo)
print("3ª forma:" + nome + sobrenome)
print("4ª forma:" + nome + " " + sobrenome)
print("5ª forma:" + nome, sobrenome )
print("6ª forma: %s" % nome_completo)
print("7ª forma: %s %s" % (nome, sobrenome))
print(f"8ª forma: {nome} {sobrenome}") 
print("9ª forma: {} {}".format(nome, sobrenome))
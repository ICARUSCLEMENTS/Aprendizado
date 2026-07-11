# Questão 8
ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    print("Ano bissexto")
elif ano % 100 != 0:
    print("Esse ano não é bissexto")
elif ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Esse ano não é bissexto")
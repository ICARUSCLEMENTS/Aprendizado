# Questão 16
cont_div = 0
cont = 1

numero = int(input("Digite um número: "))

while cont <= numero:
    if numero % cont == 0:
        cont_div += 1
    cont += 1
if cont_div == 2:
    print("É primo")
else:
    print("Não é primo")

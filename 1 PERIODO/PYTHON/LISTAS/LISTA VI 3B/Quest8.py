#Questão 8
numero = int(input("Digite um número inteiro positivo: "))
fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print(f"O fatorial de {numero} é: {fatorial}")
# Questão 9
numero = int(input("Digite um número inteiro: "))
soma_digitos = 0

while numero != 0:
    digito = numero % 10
    soma_digitos += digito
    numero = numero // 10

print("A soma dos dígitos é:", soma_digitos)
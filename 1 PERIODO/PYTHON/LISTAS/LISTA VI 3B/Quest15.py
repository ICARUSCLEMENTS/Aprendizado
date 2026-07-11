# Questão 15
n = int(input("Digite um número inteiro: "))

a, b = 0, 1
contador = 0

while contador < n:
    print(a)
    a, b = b, a + b
    contador += 1
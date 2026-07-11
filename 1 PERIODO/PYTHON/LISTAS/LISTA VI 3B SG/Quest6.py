# Questão 6
soma = 0

while True:
    numero = int(input("Digite um número (ou 0 para terminar): "))
    if numero == 0:
        break
    
    soma += numero

print("A soma final é:", soma)
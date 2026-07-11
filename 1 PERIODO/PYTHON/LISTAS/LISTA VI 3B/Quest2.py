# Questão 2
soma = 0
contador = 1

while contador <= 100:
    if contador % 2 == 0:
        soma += contador
    contador += 1

print(f"A soma de todos os números pares de 1 a 100 é: {soma}")
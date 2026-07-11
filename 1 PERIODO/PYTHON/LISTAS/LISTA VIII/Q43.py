import random

numeros = [random.randint(1, 100) for _ in range(20)]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números ímpares:", impares)
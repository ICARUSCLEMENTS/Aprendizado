contador = 0
i = 1

while i <= 100:
    if i % 2 == 0:
        contador += 1
    i += 1

print(f"Existem {contador} números pares.")
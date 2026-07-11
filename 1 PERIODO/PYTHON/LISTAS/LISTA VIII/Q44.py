numeros = [1, 2, 2, 3, 4, 4, 5]
unicos = []

for num in numeros:
    if num not in unicos:
        unicos.append(num)

print("Lista sem duplicados:", unicos)
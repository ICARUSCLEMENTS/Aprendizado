lista = [5, 3, 8, 6, 2]

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

print(lista)

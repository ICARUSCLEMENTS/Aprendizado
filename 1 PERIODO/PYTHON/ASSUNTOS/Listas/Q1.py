L = [5, 6, 4, 3, 10, 16, 2, 1]
maior = L[0]
menor = L[0]
for i in L:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(maior)
print(menor)

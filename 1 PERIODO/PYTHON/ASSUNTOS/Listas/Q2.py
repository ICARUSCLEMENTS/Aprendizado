T = [ -10, -8, 0, 1, 2, 5, -2, -4]
maior = T[0]
menor = T[0]

soma = 0

for i in T:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

for j in T:
    soma += j

print(" Maior:", maior, "| Menor: ", menor, "| Média:", soma/len(T))

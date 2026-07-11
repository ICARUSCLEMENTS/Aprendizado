L = []
con = 1

while con <= 10:
    p = int(input(f"Digite o número {con}: "))
    L.append(p)
    con += 1

maior = L[0]
menor = L[0]
soma = 0
for i in L:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print("Maior:", maior, "| Menor:", menor,)
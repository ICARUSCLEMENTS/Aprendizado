L = []
con = 1
soma = 0

while con <= 10:
    p = int(input(f"Digite o número {con}: "))
    L.append(p)
    con += 1

for i in L:
    soma += i
print(soma)
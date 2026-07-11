L = []
con = 1

while con <= 10:
    p = int(input(f"Digite o número {con}: "))
    L.append(p)
    con += 1

print("Números na lista", L)
for i in L:
    print(i * 2)

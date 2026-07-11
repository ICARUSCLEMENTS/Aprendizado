L = []
con = 1

while con <= 10:
    p = int(input(f"Digite o número {con}: "))
    L.append(p)
    con += 1


for i in L:
    if i == 200:
        print("200 está na lista! E está no indice", L.index(200))
        break

if 200 not in L:
    print("Elemento não encontrado!")
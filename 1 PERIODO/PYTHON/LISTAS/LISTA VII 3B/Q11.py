L = []
con = 1

while con <= 10:
    p = int(input(f"Digite o número {con}: "))
    L.append(p)
    con += 1

for i in L:
    if i % 2 == 0:
        print(i)

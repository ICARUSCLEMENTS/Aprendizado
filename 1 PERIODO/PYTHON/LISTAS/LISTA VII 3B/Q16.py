L = []
con = 1

while con <= 3:
    p = int(input(f"Digite o número {con}: "))
    L.append(p)
    con += 1

print(sorted(L))
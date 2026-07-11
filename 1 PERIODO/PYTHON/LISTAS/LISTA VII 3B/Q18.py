L = [1, 2, 2, 3, 3, 4]
ant = ""

for i in L:
    if L[i] == L[L.index(i) - 1]:
        del L[i]

for i in L:
    if ant == i:
        del L[i]
    else:
        ant = i

print(L)
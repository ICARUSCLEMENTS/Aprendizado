n = int(input("Digite o termo: "))
contador = 0
listh = []

while contador < n:
    contador +=1
    print(contador)
    h = 1/contador
    listh.append(h)

print(round(sum(listh),2))
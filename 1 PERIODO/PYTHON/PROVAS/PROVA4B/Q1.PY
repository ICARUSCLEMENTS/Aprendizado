def maior(lista):
    maiorvalor = lista[0]
    for i in lista:
        if i > maiorvalor:
            maiorvalor = i
    
    return maiorvalor

def menor(lista):
    menorvalor = lista[0]
    for i in lista:
        if i < menorvalor:
            menorvalor = i
    
    return menorvalor

def media(lista):
    num = 0
    soma = 0
    for i in lista:
        num += 1
    

    for j in lista:
        soma += j
    
    return soma/num

lista = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    lista.append(num)

print(f"Maior: {maior(lista)}")
print(f"Menor: {menor(lista)}")
print(f"Média: {media(lista)}")






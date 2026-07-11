lista = []

while True:
    numlist = int(input("Digite o número ou '0' para finalizar: "))
    if numlist != 0:
        lista.append(numlist)
    else:
        break

while True:
    procu = int(input(f"Digite qual número você quer saber(de 1 a {len(lista)}) ou '0' para sair: "))
    if procu == 0:
        break
    print(f"O número é: {lista[procu - 1]}")
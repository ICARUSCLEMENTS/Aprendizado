Lista = []

while True:
    lisr = int(input("Digite um número para incrementar(0 sai): "))
    if lisr == 0:
        break
    Lista.append(lisr)

listaimpar = []
listapar = []

for i in Lista:
    if i % 2 == 0:
        listapar.append(i)
    else:
        listaimpar.append(i)

print(listaimpar)
print(listapar)

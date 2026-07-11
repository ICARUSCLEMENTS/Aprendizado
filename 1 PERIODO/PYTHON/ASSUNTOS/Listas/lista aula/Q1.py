lista = []
contador = 1
while contador < 4:
    numero = int(input(f"Digite o {contador}º número: "))
    lista.append(numero)
    contador += 1

print(lista[0], lista[1], lista[2])
print(lista)
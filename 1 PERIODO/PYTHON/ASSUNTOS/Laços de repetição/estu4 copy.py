contador = 0
temperatura = []


while True:
    temp = float(input("Digite a temperatura: "))
    temperatura.append(temp)
    x = int(input("prosseguir"))
    if x == 0:
        break

aux = temperatura[0]
controlador = 1
tamanhodalista = len(temperatura)
while controlador < tamanhodalista:
    if aux < temperatura[controlador]:
        aux = temperatura[controlador]
    controlador += 1

print(aux)

while controlador < tamanhodalista:
    if aux > temperatura[controlador]:
        aux = temperatura[controlador]
    controlador += 1


print(aux)
print(min(temperatura))
print(max(temperatura))
# Questão 14
s = 0
somaimp = 0
pares = 0
impares = 0
while True:
    num = int(input("Digite um número (ou '0' para terminar): "))
    if num == 0:
        break
    s += num
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
        somaimp += num

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Soma de todos os números: {s}")
print(f"Soma dos números ímpares: {somaimp}")
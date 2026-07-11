# Questão 20
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    mmc = num1
else:
    mmc = num2

while True:
    if mmc % num1 == 0 and mmc % num2 == 0:
        break
    mmc += 1

print(f"O MMC de {num1} e {num2} é: {mmc}")
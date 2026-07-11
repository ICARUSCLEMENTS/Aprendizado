# Questão 4
num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num2 < num > num3:
    print("O primeiro número é maior")
elif num < num2 > num3:
    print("O segundo número é maior")
else:
    print("O terceiro número é maior")
num = []
for i in range(5):
    numero = int(input(f"Digite o número {i+1}: "))
    num.append(numero)

print(f"A soma dos números é: {sum(num)}")
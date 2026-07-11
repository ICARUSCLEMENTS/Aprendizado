list = []

while True:
    numint = int(input("Digite um número inteiro POSITIVO ou 0 para finalizar: "))
    list.append(numint)
    if numint == 0:
        break
    elif numint < 0:
        print("Digite um número positivo!")
        list.pop()

print(f"A soma dos números é: {sum(list)}")
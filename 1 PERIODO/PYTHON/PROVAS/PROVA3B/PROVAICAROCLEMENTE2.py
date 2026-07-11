numcon = int(input("Digite um número que queira fazer a contagem: "))
contador = 0

if numcon > 0:
    while contador < numcon:
        print(numcon)
        numcon -= 1
    print("Contagem finalizada!")
else:
    print("Digite um número positivo!")
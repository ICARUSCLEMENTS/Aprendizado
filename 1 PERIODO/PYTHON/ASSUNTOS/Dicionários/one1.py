import random

print("Bem-vindo ao jogo da memória")
print("Jogo da memória")
print("")
numeros = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
random.shuffle(numeros)
num = ["*"] * 11
while True:
    print("tentativa: ", num)
    p1 = int(input("Digite a primeira posição(1 a 11): "))
    p2 = int(input("Digite a segunda posição(1 a 11): "))
    if p1 == p2:
        print("Posições iguais. Digite novamente")
    elif num[p1 - 1] != "*" or num[p2 - 1] != "*":
        print("Posições já descobertas. Digite novamente")
    else:
        num[p1 - 1] = numeros[p1 - 1]
        num[p2 - 1] = numeros[p2 - 1]

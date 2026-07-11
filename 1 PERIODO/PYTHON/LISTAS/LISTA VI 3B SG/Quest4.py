# Questão 4
import random

secreto = random.randint(1, 20)
tentativas = 5

while True:
    adviin = int(input("Digite um número entre 1 e 20: "))
    if adviin > 20:
        print("Esse número não está entre 1 e 20!")
    elif adviin < 1:
        print("Esse número não está entre 1 e 20!")
    elif adviin > secreto:
        print("Esse numero é maior")
    elif adviin < secreto:
        print("Esse número é menor")
    else:
        print(f"Você acertou o número! Ele é {secreto}")
        break
    tentativas -= 1
    if tentativas > 0:
        print(f"Você ainda tem {tentativas} tentativas restantes.")
    else:
        print(f"Suas tentativas acabaram! O número secreto era {secreto}.")
        break
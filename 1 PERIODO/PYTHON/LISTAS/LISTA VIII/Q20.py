import random

num = random.randint(1, 50)
tentativas = 0
palpi = 0

print("Tente adivinhar o número entre 1 e 50.")

while palpi != num:
    palpi = int(input("Digite seu palpite: "))
    tentativas += 1
    if palpi < num:
        print("Muito baixo! Tente novamente.")
    elif palpi > num:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
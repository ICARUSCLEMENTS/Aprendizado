import os
while True:
    contador = 1
    try:
        secreto = int(input("Digite o númeto secreto: "))
        print("ou digite uma letra para finalizar")
    except ValueError:
        print("Finalizado")
        break
    os.system('cls')
    while contador <= 6:
        adv = int(input("Digite um número para tentar adivinhar: "))
        if adv > secreto:
            print(f"EROOU!!! Tentativas Restantes {5 - contador}. O número secreto é menor")
            contador += 1
        elif adv < secreto:
            print(f"EROOU!!! Tentativas Restantes {5 - contador}. O número secreto é maior")
            contador += 1
        else:
            os.system('cls')
            print(f"Acertou! O número é {secreto}")
            break
        if contador == 6:
            os.system('cls')
            print("Não há mais tentativas!")
            break
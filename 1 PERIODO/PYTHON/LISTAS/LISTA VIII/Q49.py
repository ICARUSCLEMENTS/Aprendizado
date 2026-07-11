import random

palavras = ["python", "programação", "desafio", "inteligência", "artificial"]
palavra = random.choice(palavras)
palavra_escondida = ["_"] * len(palavra)
tentativas = 6

print("Bem-vindo ao jogo da forca!")

while tentativas > 0 and "_" in palavra_escondida:
    print(" ".join(palavra_escondida))
    letra = input("Digite uma letra: ").lower()
    
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_escondida[i] = letra
    else:
        tentativas -= 1
        print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")
        
if "_" not in palavra_escondida:
    print(f"Parabéns! Você adivinhou a palavra: {''.join(palavra_escondida)}")
else:
    print(f"Que pena! Suas tentativas acabaram. A palavra era: {palavra}")

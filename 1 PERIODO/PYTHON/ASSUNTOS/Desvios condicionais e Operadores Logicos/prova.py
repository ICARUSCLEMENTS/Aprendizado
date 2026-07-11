# Começo
import os
import math

os.system('cls')
print("-"*60)
print("Bem vindo a prova de Ícaro Clemente!")
print("-"*60)
print("1 - Verificar se um número é impar ou par.")
print("2 - Calcular o dobro e metade de um número.")
print("3 - Identificar o sucessor e o antecessor de um número")
print("4 - Calcular a potência de um número (solicite a base e o expoente)")
print("5 - Calcular a raiz quadrada de um número.")
print("6- Calcular o módulo de um número.")
print("0 - Sair do programa")
print("-"*60)

opcoes = input("Digite a opção desejada acima: ")

if opcoes == "1":
    os.system('cls')
    print("-"*60)
    parouimpar = int(input("Digite o número que você que saber se é par ou impar: "))
    print("-"*60)
    if parouimpar % 2 == 0:
        print(f"{parouimpar} é par")
    else:
        print(f"{parouimpar} é ímpar")
    print("-"*60)

elif opcoes == "2":
    os.system('cls')
    print("-"*60)
    dobrooumetade = float(input("Digite o número desejado para saber o dobro e a metade: "))
    os.system('cls')
    dobro = dobrooumetade * 2
    metade = dobrooumetade / 2
    print("-"*60)
    print(f"O dobro é {dobro} e a metade é {metade}")
    print("-"*60)

elif opcoes == "3":
    os.system('cls')
    print("-"*60)
    suouante = int(input("Digite o número para saber o sucessor e o antecessor: "))
    suce = suouante + 1
    ante = suouante - 1
    os.system('cls')
    print("-"*60)
    print(f"O sucessor é {suce} e o antecessor é {ante}")
    print("-"*60)

elif opcoes == "4":
    os.system('cls')
    print("-"*60)
    base = int(input("Digite a base: "))
    expo = int(input("Digite o expoente: "))
    os.system('cls')
    print("-"*60)
    print("O resultado é:", math.pow(base, expo))
    print("-"*60)

elif opcoes == "5":
    os.system('cls')
    print("-"*60)
    raiz = int(input("Digite para saber a raiz quadrada: "))
    print("-"*60)
    print(f"A raiz quadrada de {raiz} é:", math.sqrt(raiz))
    print("-"*60)
elif opcoes == "6":
    os.system('cls')
    print("-"*60)
    modulo = int(input("Digite o número para saber do módulo: "))
    os.system('cls')
    print("-"*60)
    print(f"O módulo de {modulo} é:", math.fabs(modulo))
    print("-"*60)

elif opcoes == "0":
    os.system('cls')
    print("-"*80)
    print("Você saiu do programa com sucesso! Obrigado por estar usando nosso programa.")
    print("-"*80)

else:
    os.system('cls')
    print("-"*60)
    print("ERRO! Digite uma das opções por favor.")
    print("-"*60)
import math
import os

os.system('cls')

print("-"*40)
print("Seja bem-vindo a calculadora...")
print("-"*40)
print("Escolha uma das opções:")
print("1. Verificar se um número é par ou impar.")
print("2. Verificar se um número é divisível por 5")
print("3. Calcular a média entre dois números.")
print("0. Sair")
print("-"*40)

num = input("Digite uma das opções: ")

if num == "1":
    os.system('cls')
    print("-"*40)
    print("Opção Escolhida: '1. Verificar se um número é par ou impar.'")
    print("-"*40)
    per = int(input("Digite um número inteiro: "))
    if per % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
elif num == "2":
    os.system('cls')
    print("-"*40)
    print("Opção Escolhida: '2. Verificar se um número é divisível por 5'")
    print("-"*40)
    per = int(input("Digite um número inteiro: "))
    if per % 5 == 0:
        print("Divisível")
    else:
        print("Não Divisível")
elif num == "3":
    os.system('cls')
    print("-"*40)
    print("Opção Escolhida: '3. Calcular a média entre dois números.'")
    print("-"*40)
    per = int(input("Digite um número inteiro: "))
    per2 = int(input("Digite um número inteiro: "))
    media = (per + per2) / 2
    print(media)
elif num == "0":
    os.system('cls')
    print("-"*40)
    print("Obrigado!")
    print("-"*40)
else:
    os.system('cls')
    print("-"*40)
    print("Digite um número válido!")
    print("-"*40)
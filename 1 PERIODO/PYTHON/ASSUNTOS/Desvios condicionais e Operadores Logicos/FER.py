import os
os.system('cls')
a = 10
b = 5

if not (a > 15) and b < 10:
    print("1-", not (a > 15))
    print("2-", b < 10)
    print("3-", not (a > 15) and b < 10)
    print("Condição verdadeira: a não é maior que 15 e b é menor que 10.")
else:
    print("Condição falsa.")
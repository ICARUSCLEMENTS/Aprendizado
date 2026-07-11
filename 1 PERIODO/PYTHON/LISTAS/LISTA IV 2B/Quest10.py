# Questão 10
num = int(input("Digite um número: "))
ca = num >= 10
# "Computador, o número que eu digitei é maior ou igual 10?"
ca2 = num <= 20
# "Computador, o número que eu digitei é menor ou igual a 20?"
tru = ca and ca2

if tru == True:
    print("Dentro do intervalo")
# Questão 16
idade = int(input("Digite sua idade: "))
idade1 = idade >= 13
# "Computador, a idade que eu digitei é maior ou igual 13?"
idade2 = idade <=19
# "Computador, a idade que eu digitei é menor ou igual a 19?"
tru = idade1 and idade2

if tru == True:
    print("Adolescente")
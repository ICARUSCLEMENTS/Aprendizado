# Questão 2
idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Criança")
elif 12 <= idade <= 17:
    print("Adolescente")
else:
    print("Adulto")
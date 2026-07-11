# Questão 18
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

contador = 0
termo = primeiro_termo

while contador < 10:
    print(termo)
    termo += razao
    contador += 1
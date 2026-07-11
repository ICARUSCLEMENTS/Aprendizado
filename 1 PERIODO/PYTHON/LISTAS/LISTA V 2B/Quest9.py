# Questão 9
nota = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota + nota2 + nota3)/3
print("Sua média é %.1f" % (media))

if media >= 70:
    print("Aprovado!")
elif 50 <= media <= 69:
    print("Recuperação!")
else:
    print("Reprovado")

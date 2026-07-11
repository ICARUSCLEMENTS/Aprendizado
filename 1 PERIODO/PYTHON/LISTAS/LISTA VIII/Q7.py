nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print(media)

if media >= 60:
    print("Aprovado!")

elif media >= 40:
    print("Recuperação!")

else:
    print("Reprovado!")

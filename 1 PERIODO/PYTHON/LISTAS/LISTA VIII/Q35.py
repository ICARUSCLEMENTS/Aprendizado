notasalunos = {
    "Alice": 8.5,
    "Bruno": 9.0,
    "Carlos": 7.5
}

nomealuno = input("Digite o nome do aluno: ")

if nomealuno in notasalunos:
    print(f"A nota de {nomealuno} é {notasalunos[nomealuno]}")
else:
    print(f"Aluno {nomealuno} não encontrado.")

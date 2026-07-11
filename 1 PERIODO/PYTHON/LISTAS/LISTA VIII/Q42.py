alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para terminar): ")
    if nome.lower() == 'sair':
        break
    idade = int(input("Digite a idade do aluno: "))
    notas = list(map(float, input("Digite as notas do aluno separadas por espaço: ").split()))
    alunos[nome] = {'idade': idade, 'notas': notas}

consulta = input("Digite o nome do aluno para consulta: ")
if consulta in alunos:
    print(f"Nome: {consulta}")
    print(f"Idade: {alunos[consulta]['idade']}")
    print(f"Notas: {alunos[consulta]['notas']}")
else:
    print(f"Aluno {consulta} não encontrado.")

turma = []

def cadastrar_aluno(nome, matricula, notas):
    aluno = {"nome": nome, "matricula": matricula, "notas": notas}
    turma.append(aluno)

def calcular_media(notas):
    return sum(notas) / len(notas)

def exibir_boletim(matricula):
    for aluno in turma:
        if aluno["matricula"] == matricula:
            media = calcular_media(aluno["notas"])
            print(f"Nome: {aluno['nome']}")
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Notas: {aluno['notas']}")
            print(f"Média: {media:.2f}")
            return
    print("Aluno não encontrado.")

def gerar_estatisticas_da_turma():
    if not turma:
        print("Nenhum aluno cadastrado.")
        return

    medias = [calcular_media(aluno["notas"]) for aluno in turma]
    media_geral = sum(medias) / len(medias)
    maior_media = max(medias)
    menor_media = min(medias)

    aluno_maior_media = None
    aluno_menor_media = None
    aprovados = []

    for aluno in turma:
        media = calcular_media(aluno["notas"])
        if media == maior_media:
            aluno_maior_media = aluno
        if media == menor_media:
            aluno_menor_media = aluno
        if media >= 7:
            aprovados.append(aluno["nome"])

    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Aluno com maior média: {aluno_maior_media['nome']} ({maior_media:.2f})")
    print(f"Aluno com menor média: {aluno_menor_media['nome']} ({menor_media:.2f})")
    print(f"Lista de aprovados: {', '.join(aprovados) if aprovados else 'Nenhum aluno aprovado'}")

while True:
    print("1. Cadastrar aluno")
    print("2. Exibir boletim")
    print("3. Gerar estatísticas da turma")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        matricula = input("Matrícula do aluno: ")
        notas = [float(input(f"{i+1}ª Nota: ")) for i in range(3)]
        cadastrar_aluno(nome, matricula, notas)
    elif opcao == "2":
        matricula = input("Digite a matrícula do aluno: ")
        exibir_boletim(matricula)
    elif opcao == "3":
        gerar_estatisticas_da_turma()
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
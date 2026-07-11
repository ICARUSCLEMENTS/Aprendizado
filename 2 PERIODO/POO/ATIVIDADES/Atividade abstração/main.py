from system import Figurinha
from system import Pacotinho
from system import MinhaColecao

fig1 = Figurinha(1, "Tema 1")
fig2 = Figurinha(2, "Tema 2")

pacotinho = Pacotinho()
pacotinho.adicionar(fig1)
pacotinho.adicionar(fig2)
pacotinho.listar()

colecao = MinhaColecao()

print(f"Figurinhas coladas: {len(colecao.figurinhas)}")
print(f"Figurinhas faltantes: {colecao.faltantes()}")

colecao.colar(fig1)
colecao.colar(fig2)

print(f"Figurinhas coladas: {len(colecao.figurinhas)}")
print(f"Figurinhas faltantes: {colecao.faltantes()}")

print("-" * 100)

from system import Aluno
from system import Professor
from system import Escola

aluno1 = Aluno("João", 9)
aluno2 = Aluno("Maria", 4)
aluno3 = Aluno("Pedro", 7)

print(f"Aluno: {aluno1.nome}, Estado: {'Aprovado' if aluno1.foi_aprovado() else 'Reprovado'}")
print(f"Aluno: {aluno2.nome}, Estado: {'Aprovado' if aluno2.foi_aprovado() else 'Reprovado'}")
print(f"Aluno: {aluno3.nome}, Estado: {'Aprovado' if aluno3.foi_aprovado() else 'Reprovado'}")

prof1 = Professor("Prof. Demetrios")
prof1.adicionar_aluno(aluno1)
prof1.adicionar_aluno(aluno2)
prof1.adicionar_aluno(aluno3)

print(f"Média da turma: {prof1.media_da_turma():.1f}")
print(f"Alunos aprovados: {', '.join(prof1.aprovados())}")

prof2 = Professor("Prof. Raphael", [])
prof2.adicionar_aluno(aluno1)
prof2.adicionar_aluno(aluno2)


print(f"Média da turma: {prof2.media_da_turma():.1f}")
print(f"Alunos aprovados: {prof2.aprovados()}")

escola1 = Escola([prof1, prof2])
escola1.relatorio_geral()

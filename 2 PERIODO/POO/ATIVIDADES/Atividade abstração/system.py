class Figurinha:
    def __init__(self, numero, tema):
        self.numero = numero
        self.tema = tema
    
    def mostrar(self):
        print(f"Figurinha {self.numero} - {self.tema}")

class Pacotinho:
    def __init__(self):
        self.figurinhas = []
    
    def adicionar(self, figurinha):
        self.figurinhas.append(figurinha)
    
    def listar(self):
        print("Pacotinho:")
        for figurinha in self.figurinhas:
            figurinha.mostrar()

class MinhaColecao:
    def __init__(self, figurinhas=[]):
        self.figurinhas = figurinhas
        self.pacotinhos = []
    
    def colar(self, figurinha):
        self.figurinhas.append(figurinha)
    
    def faltantes(self):
                return 10 - len(self.figurinhas)


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def foi_aprovado(self):
        return self.nota >= 6

class Professor:
    def __init__(self, nome, lista_alunos=[]):
        self.nome = nome
        self.lista_alunos = lista_alunos
    
    def adicionar_aluno(self, aluno):
        self.lista_alunos.append(aluno)
    
    def media_da_turma(self):
        total = 0
        for aluno in self.lista_alunos:
            total += aluno.nota
        media = total / len(self.lista_alunos)
        return media
    
    def aprovados(self):
        aprovados = []
        for aluno in self.lista_alunos:
            if aluno.foi_aprovado():
                aprovados.append(aluno.nome)
        return aprovados
    


class Escola:
    def __init__(self, professores=[]):
        self.professores = professores
    
    def relatorio_geral(self):
        for professor in self.professores:
            print(f"Professor: {professor.nome}")
            print("Quantidade de alunos:", len(professor.lista_alunos))
            print(f"Média da turma: {professor.media_da_turma():.1f}")
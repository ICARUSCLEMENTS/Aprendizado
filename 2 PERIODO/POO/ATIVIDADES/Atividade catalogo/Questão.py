class Filme:
    def __init__(self, titulo, ano, avaliacao):
        self.titulo = titulo
        self.ano = ano
        if 0 <= avaliacao <= 5:
            self.avaliacao = avaliacao
        else:
            self.avaliacao = 0

    def dar_nota(self, nota):
        if 0 <= nota <= 5:
            self.avaliacao = nota

class playlist:
    def __init__(self, nome, filmes=[]):
        self.nome = nome
        self.filmes = filmes
    
    def adicionar_filme(self, filme):
        if isinstance(filme, Filme):
            self.filmes.append(filme)
        else:
            print("Erro ao tentar adicionar o filme. O filme procurado não existe.")
    
    def remover_filme(self, filme):
        if filme in self.filmes:
            self.filmes.remove(filme)
        else:
            print("Erro ao tentar remover o filme. O filme procurado não existe.")

    def mostrar(self):
        for filme in self.filmes:
            print(f"Titulo: {filme.titulo}, Ano: {filme.ano}, Avaliacao: {filme.avaliacao}")

f1 = Filme("Vingadores", 2012, 4.5)
f2 = Filme("Vingadores Ultimato", 2019, 4.8)

p1 = playlist("Playlist 1")
p2 = playlist("Playlist 2")

p1.adicionar_filme(f1)
p2.adicionar_filme(f1)

f1.dar_nota(4.5)
p1.mostrar()
p2.mostrar()

print(id(p1.filmes[0]))
print(id(p2.filmes[0]))

p1.remover_filme(f1)
p1.mostrar()
p2.mostrar()

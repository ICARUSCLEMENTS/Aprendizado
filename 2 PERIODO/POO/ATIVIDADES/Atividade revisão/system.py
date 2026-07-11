class livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostrar_dados(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}"

class biblioteca:
    def __init__(self, nome, livros=[]):
        self.nome = nome
        self.livros = livros

    def adicionar_livro(self, livro):
        for l in self.livros:
            if l.titulo == livro.titulo:
                return "Livro já existe na biblioteca"
        self.livros.append(livro)

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                return self.livro.mostrar_dados()
        return "Livro não encontrado na biblioteca"

    def mostrar_livros(self):
        for livro in self.livros:
            print(livro.mostrar_dados())

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return "Livro não encontrado"


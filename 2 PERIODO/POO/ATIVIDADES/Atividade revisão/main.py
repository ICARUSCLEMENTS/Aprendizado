from system import livro
from system import biblioteca

l1 = livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
l2 = livro("1984", "George Orwell", 1949)

print(f"Título: {l1.titulo}, Autor: {l1.autor}, Ano: {l1.ano}")
print(f"Título: {l2.titulo}, Autor: {l2.autor}, Ano: {l2.ano}")

l3 = l1
print(f"Título: {l3.titulo}, Autor: {l3.autor}, Ano: {l3.ano}")
l3.ano = 1955
print(f"Título: {l3.titulo}, Autor: {l3.autor}, Ano: {l3.ano}")

print(id(l1))
print(id(l3))
print(id(l1) == id(l3))

pl1 = l1.mostrar_dados()
print(pl1)
print("_" * 100)

b1 = biblioteca("Biblioteca Central", [l1, l2])
b1.mostrar_livros()

l4 = livro("O Hobbit", "J.R.R. Tolkien", 1937)
b1.adicionar_livro(l4)
b1.mostrar_livros()

b1.livros[0].autor = "Ícaro"
print(id(b1.livros[0]), b1.livros[0].autor)
print(id(l1.autor), l1.autor)

b1.remover_livro("1984")
b1.mostrar_livros()


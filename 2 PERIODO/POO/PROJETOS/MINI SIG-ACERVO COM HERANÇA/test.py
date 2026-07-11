from datetime import datetime, timedelta
from rich.console import Console
from models import BaseEntity, Obra, Usuario, Emprestimo
from core import Acervo

console = Console()

acervo =  Acervo()

obra1 = Obra("1984", "George Orwell", 1949, "Romance", quantidade=3)
obra2 = Obra("Dom Casmurro", "Machado de Assis", 1899, "Romance", quantidade=2)

acervo.adicionar(obra1)
acervo.adicionar(obra2)

usuario1 = Usuario("Alice", "alice@example.com")
usuario2 = Usuario("Bruno", "bruno@example.com")

emprestimo1 = acervo.emprestar(obra1, usuario1, dias=7)
emprestimo2 = acervo.emprestar(obra2, usuario2, dias=5)

data_devolucao_atrasada = emprestimo1.data_prev_devol + timedelta(days=3)
acervo.devolver(emprestimo1, data_devolucao_atrasada)

data_devolucao_pontual = emprestimo2.data_prev_devol
acervo.devolver(emprestimo2, data_devolucao_pontual)

console.print("\n📚 [bold underline]Inventário Atualizado:[/bold underline]")
console.print(acervo.relatorio_inventario())

console.print("\n📄 [bold underline]Histórico de Empréstimos - Alice:[/bold underline]")
console.print(acervo.historico_usuario(usuario1))

console.print("\n📄 [bold underline]Histórico de Empréstimos - Bruno:[/bold underline]")
console.print(acervo.historico_usuario(usuario2))

multa = acervo.valor_multa(emprestimo1, data_devolucao_atrasada)
console.print(f"\n💸 [bold red]Multa de Alice por atraso:[/bold red] R$ {multa:.2f}")
from datetime import datetime, timedelta
from rich.table import Table
from rich.console import Console
from models import Obra, Usuario, Emprestimo

class Acervo:
    """
    Gerencia o acervo de obras e os empréstimos realizados.
    """

    def __init__(self):
        """
        Inicializa o acervo com estoque vazio e lista de empréstimos.
        """
        self.estoque = {}
        self.emprestimos = []

    def __iadd__(self, obra):
        """
        Adiciona uma obra ao acervo.

        Args:
            obra (Obra): Obra a ser adicionada.

        Returns:
            Acervo: Instância atualizada do acervo.
        """
        if obra.id in self.estoque:
            self.estoque[obra.id].quantidade += obra.quantidade
        else:
            self.estoque[obra.id] = obra
        return self

    def __isub__(self, obra):
        """
        Remove uma quantidade da obra do acervo.

        Args:
            obra (Obra): Obra a ser removida.

        Returns:
            Acervo: Instância atualizada do acervo.
        """
        if obra.id in self.estoque:
            if self.estoque[obra.id].quantidade > obra.quantidade:
                self.estoque[obra.id].quantidade -= obra.quantidade
            else:
                del self.estoque[obra.id]
        return self

    def adicionar(self, obra):
        """
        Adiciona uma obra ao acervo.

        Args:
            obra (Obra): Obra a ser adicionada.
        """
        self += obra

    def remover(self, obra):
        """
        Remove uma obra do acervo.

        Args:
            obra (Obra): Obra a ser removida.
        """
        self -= obra

    def emprestar(self, obra, usuario, dias=7):
        """
        Realiza o empréstimo de uma obra para um usuário.

        Args:
            obra (Obra): Obra a ser emprestada.
            usuario (Usuario): Usuário que fará o empréstimo.
            dias (int): Prazo em dias para devolução.

        Returns:
            Emprestimo: Objeto representando o empréstimo.
        """
        if obra.id not in self.estoque or self.estoque[obra.id].quantidade <= 0:
            raise ValueError("Obra não disponível para empréstimo.")
        data_retirada = datetime.now()
        data_prev_devol = data_retirada + timedelta(days=dias)
        emprestimo = Emprestimo(obra, usuario, data_retirada, data_prev_devol)
        self -= obra
        self.emprestimos.append(emprestimo)
        return emprestimo

    def devolver(self, emprestimo, data_dev):
        """
        Registra a devolução de uma obra emprestada.

        Args:
            emprestimo (Emprestimo): Empréstimo a ser encerrado.
            data_dev (datetime): Data real de devolução.
        """
        if emprestimo.obra.id not in self.estoque:
            self.estoque[emprestimo.obra.id] = emprestimo.obra
        self.estoque[emprestimo.obra.id].quantidade += 1
        emprestimo.marcar_devolucao(data_dev)

    def renovar(self, emprestimo, dias_extra):
        """
        Renova o prazo de devolução de um empréstimo.

        Args:
            emprestimo (Emprestimo): Empréstimo a ser renovado.
            dias_extra (int): Dias adicionais para devolução.
        """
        if emprestimo.obra.id not in self.estoque:
            raise ValueError("Obra não disponível para renovação.")
        emprestimo.data_prev_devol += timedelta(days=dias_extra)

    def valor_multa(self, emprestimo, data_ref):
        """
        Calcula o valor da multa por atraso.

        Args:
            emprestimo (Emprestimo): Empréstimo a ser avaliado.
            data_ref (datetime or date): Data de referência.

        Returns:
            float: Valor da multa em reais.
        """
        dias_atraso = emprestimo.dias_atraso(data_ref)
        return dias_atraso * 1.00 if dias_atraso > 0 else 0.00

    def relatorio_inventario(self):
        """
        Gera uma tabela com o inventário atual do acervo.

        Returns:
            Table: Tabela formatada com as obras e quantidades.
        """
        table = Table(title="Inventário do Acervo")
        table.add_column("ID", style="cyan")
        table.add_column("Título", style="magenta")
        table.add_column("Autor", style="green")
        table.add_column("Ano", style="yellow")
        table.add_column("Categoria", style="blue")
        table.add_column("Quantidade", style="red")

        for obra in self.estoque.values():
            table.add_row(
                str(obra.id),
                obra.titulo,
                obra.autor,
                str(obra.ano),
                obra.categoria,
                str(obra.quantidade)
            )
        return table

    def relatorio_debitos(self):
        """
        Gera uma tabela com os débitos (atrasos) dos usuários.

        Returns:
            Table: Tabela com informações de atraso e multas.
        """
        table = Table(title="Débitos de Usuários")
        table.add_column("ID", style="cyan")
        table.add_column("Usuário", style="magenta")
        table.add_column("Obra", style="green")
        table.add_column("Data Prev. Devolução", style="yellow")
        table.add_column("Dias Atraso", style="red")
        table.add_column("Valor Multa (R$)", style="blue")

        for emprestimo in self.emprestimos:
            dias_atraso = emprestimo.dias_atraso(datetime.now())
            if dias_atraso > 0:
                valor_multa = self.valor_multa(emprestimo, datetime.now())
                table.add_row(
                    str(emprestimo.id),
                    str(emprestimo.usuario),
                    str(emprestimo.obra),
                    emprestimo.data_prev_devol.strftime('%d/%m/%Y'),
                    str(dias_atraso),
                    f"{valor_multa:.2f}"
                )
        return table

    def historico_usuario(self, usuario):
        """
        Gera o histórico de empréstimos de um usuário.

        Args:
            usuario (Usuario): Usuário a ser consultado.

        Returns:
            Table: Tabela com os empréstimos realizados pelo usuário.
        """
        table = Table(title=f"Histórico de Empréstimos - {usuario.nome}")
        table.add_column("ID", style="cyan")
        table.add_column("Obra", style="magenta")
        table.add_column("Data Retirada", style="green")
        table.add_column("Data Prev. Devolução", style="yellow")
        table.add_column("Data Real Devolução", style="red")

        for emprestimo in self.emprestimos:
            if emprestimo.usuario == usuario:
                data_real = emprestimo.data_dev_real.strftime('%d/%m/%Y') if emprestimo.data_dev_real else "—"
                table.add_row(
                    str(emprestimo.id),
                    str(emprestimo.obra),
                    emprestimo.data_retirada.strftime('%d/%m/%Y'),
                    emprestimo.data_prev_devol.strftime('%d/%m/%Y'),
                    data_real
                )
        return table

    def _valida_obra(self, obra):
        """
        Valida se o objeto é uma instância da classe Obra.

        Args:
            obra (Obra): Objeto a ser validado.

        Raises:
            TypeError: Se o objeto não for uma instância de Obra.
        """
        if not isinstance(obra, Obra):
            raise TypeError("O objeto deve ser uma instância de Obra.")

    def _relatorio_builder(self, titulo):
        """
        Cria uma instância da classe interna RelatorioBuilder_ para gerar relatórios com título personalizado.

        Args:
            titulo (str): Título do relatório.

        Returns:
            RelatorioBuilder_: Instância da classe interna de relatório.
        """
        class RelatorioBuilder_:
            """
            Classe interna responsável por gerar relatórios formatados do acervo.
            """

            def __init__(self, acervo):
                """
                Inicializa o gerador de relatório.

                Args:
                    acervo (Acervo): Instância do acervo a ser relatado.
                """
                self.acervo = acervo
                self.titulo = titulo

            def gerar(self):
                """
                Imprime o relatório de inventário no console com o título definido.
                """
                console = Console()
                console.print(self.acervo.relatorio_inventario(), title=self.titulo)

        return RelatorioBuilder_(self)
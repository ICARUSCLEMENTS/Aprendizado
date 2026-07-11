import uuid
from datetime import datetime, timedelta
from rich.table import Table
from rich.console import Console

class BaseEntity:
    """
    Classe base para entidades do sistema, fornecendo um ID único e data de criação.
    """

    def __init__(self):
        """
        Inicializa a entidade com um ID único e registra a data de criação.
        """
        self.id = self._gerar_id()
        self.data_criacao = datetime.now()

    def __eq__(self, other):
        """
        Compara duas entidades com base no ID.

        Args:
            other (BaseEntity): Outra entidade para comparação.

        Returns:
            bool: True se os IDs forem iguais, False caso contrário.
        """
        return isinstance(other, BaseEntity) and self.id == other.id

    def _gerar_id(self):
        """
        Gera um identificador único (UUID4).

        Returns:
            UUID: Identificador único.
        """
        return uuid.uuid4()

class Obra(BaseEntity):
    """
    Representa uma obra do acervo, como um livro ou revista.
    """

    def __init__(self, titulo, autor, ano, categoria, quantidade=1):
        """
        Inicializa uma nova obra.

        Args:
            titulo (str): Título da obra.
            autor (str): Nome do autor.
            ano (int): Ano de publicação.
            categoria (str): Categoria da obra.
            quantidade (int): Quantidade de exemplares disponíveis.
        """
        super().__init__()
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.quantidade = quantidade

    def disponivel(self, estoque):
        """
        Verifica se há exemplares disponíveis no estoque.

        Args:
            estoque (dict): Dicionário de obras no acervo.

        Returns:
            bool: True se houver exemplares disponíveis, False caso contrário.
        """
        return self.id in estoque and estoque[self.id].quantidade > 0

    def __str__(self):
        """
        Retorna uma representação textual da obra.

        Returns:
            str: Título e ano da obra.
        """
        return f"{self.titulo} ({self.ano})"

class Usuario(BaseEntity):
    """
    Representa um usuário do sistema.
    """

    def __init__(self, nome, email):
        """
        Inicializa um novo usuário.

        Args:
            nome (str): Nome do usuário.
            email (str): Endereço de e-mail.
        """
        super().__init__()
        self.nome = nome
        self.email = email

    def __lt__(self, other):
        """
        Permite ordenação alfabética de usuários pelo nome.

        Args:
            other (Usuario): Outro usuário para comparação.

        Returns:
            bool: True se o nome for menor alfabeticamente.
        """
        return isinstance(other, Usuario) and self.nome < other.nome

    def __str__(self):
        """
        Retorna o nome do usuário.

        Returns:
            str: Nome do usuário.
        """
        return self.nome

class Emprestimo(BaseEntity):
    """
    Representa um empréstimo de uma obra para um usuário.
    """

    def __init__(self, obra, usuario, data_retirada, data_prev_devol):
        """
        Inicializa um novo empréstimo.

        Args:
            obra (Obra): Obra emprestada.
            usuario (Usuario): Usuário que realizou o empréstimo.
            data_retirada (datetime): Data da retirada.
            data_prev_devol (datetime): Data prevista para devolução.
        """
        super().__init__()
        self.obra = obra
        self.usuario = usuario
        self.data_retirada = data_retirada
        self.data_prev_devol = data_prev_devol
        self.data_dev_real = None

    def marcar_devolucao(self, data_dev_real):
        """
        Registra a data real de devolução da obra.

        Args:
            data_dev_real (datetime): Data em que a obra foi devolvida.
        """
        self.data_dev_real = data_dev_real

    def dias_atraso(self, data_ref):
        """
        Calcula o número de dias de atraso com base em uma data de referência.

        Args:
            data_ref (datetime or date): Data de referência para calcular o atraso.

        Returns:
            int: Número de dias de atraso. Retorna 0 se não houver atraso.
        """

        data_ref = data_ref if isinstance(data_ref, datetime) else datetime.combine(data_ref, datetime.min.time())
        if self.data_prev_devol.date() < data_ref.date():
            return (data_ref.date() - self.data_prev_devol.date()).days
        return 0


    def __str__(self):
        """
        Retorna uma representação resumida do empréstimo.

        Returns:
            str: Título da obra e data prevista de devolução.
        """
        return f"{self.obra} ({self.data_prev_devol.strftime('%d/%m')})"

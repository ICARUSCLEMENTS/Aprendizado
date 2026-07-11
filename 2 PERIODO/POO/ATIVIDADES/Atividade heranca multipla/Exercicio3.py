import json

class LogMixin:
    def log(self, mensagem):
        print(f"LOG: {mensagem}")

class NotificacaoMixin:
    def enviar_notificacao(self, usuario, mensagem):
        print(f"Enviando notificação para {usuario}:{mensagem}")

class SerializacaoMixin:
    def salvar_como_json(self, dados, arquivo="dados.json"):
        with open(arquivo, "w") as f:
            json.dump(dados, f)
        print(f"Dados salvos em {arquivo}")

class AutenticacaoMixin:
    def verificar_senha(self, senhavalidar):
        # Simulação de verificação de senha
        if senhavalidar == self.senha:
            print("Senha correta!")
            return True
        else:
            print("Senha incorreta!")
            return False


class Usuario(LogMixin, NotificacaoMixin, SerializacaoMixin, AutenticacaoMixin):
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.log(f"Usuário {self.nome} criado.")

    def salvar_dados(self):
        dados = {"nome": self.nome, "email": self.email}
        self.salvar_como_json(dados)


usuario = Usuario("Alice", "alice@email.com", 1234)
usuario.enviar_notificacao("Alice", "Bem-vinda ao sistema!")
usuario.salvar_dados()

usuario.verificar_senha(1234)
usuario.verificar_senha(5678)

from Funcionario import Funcionario

class ControleDeBonificacoes:
    def __init__(self):
        self.__total_bonificacoes = 0
    
    def registra(self, funcionario):
        """
        Implementar:
        Deve adicionar a bonificação do funcionário ao total.
        Utilize o método get_bonificacao() do objeto funcionário.
        """
        
        self.__total_bonificacoes += funcionario.get_bonificacao()

    @property
    def total_bonificacoes(self):
        return self.__total_bonificacoes
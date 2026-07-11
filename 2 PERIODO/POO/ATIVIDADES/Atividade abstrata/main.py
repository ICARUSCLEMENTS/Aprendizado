import abc

class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo=0, limite=1000):
        self.número = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass
    
    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return f"Conta: {self.número} | Titular: {self.titular} | Saldo: {self.saldo} | Limite: {self.limite}"
    

class ContaCorrente(Conta):
    def __init__(self, titular, numero, saldo, limite=1000):
        super().__init__(titular, numero, saldo, limite=1000)
        self.tipo = "Conta Poupança"
    
    def atualiza(self, taxa):
        self.saldo *= (1 + taxa * 2)

    def deposita(self, valor):
        self.saldo += (valor * 0.9)

class ContaPoupanca(Conta):
    def __init__(self, titular, numero, saldo, limite=1000):
        super().__init__(titular, numero, saldo, limite=1000)
        self.tipo = "Conta Poupança"

    def atualiza(self, taxa):
        self.saldo *= (1 + taxa * 3)

    def deposita(self, valor):
        self.saldo += valor
    

class ContaInvestimento(Conta):
    def __init__(self, titular, numero, saldo, limite=1000):
        super().__init__(titular, numero, saldo, limite=1000)
        self.tipo = "Conta Investimento"

    def atualiza(self, taxa):
        self.saldo *= (1 + taxa * 5)

    def deposita(self, valor):
        self.saldo += valor

class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total
    
    def roda(self, conta):
        print("Saldo anterior:", conta.saldo)
        conta.atualiza(self._selic)
        self._saldo_total += conta.saldo
        print(f"Saldo atualizado: {conta.saldo}")
    
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
    
    def adiciona(self, conta):
        self.contas.append(conta)
    
    def pegaConta(self, numero):
        for conta in self.contas:
            if conta.número == numero:
                return conta
        return None

    def totalContas(self):
        return len(self.contas)

if __name__ == '__main__':
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'Maria', 2000.0)
    ci = ContaInvestimento('123-6', 'Carlos', 3000.0)

    cc.deposita(500.0)
    cp.deposita(1000.0)
    ci.deposita(1500.0)

    adc = AtualizadorDeContas(0.01)

    adc.roda(cc)
    adc.roda(cp)
    adc.roda(ci)

    print(f"Saldo total acumulado: {adc._saldo_total}")

    b1 = Banco('Inter')
    b1.adiciona(cc)
    b1.adiciona(cp)
    b1.adiciona(ci)

    print(f"Total de contas no banco {b1.nome}: {b1.totalContas()}")
    print(b1.pegaConta('123-4'))

# cc = ContaCorrente('123-4', 'João', 1000)
# cp = ContaPoupanca('123-5', 'Maria', 2000)
# ci = ContaInvestimento('123-6', 'Carlos', 3000)

# cc.deposita(500.0)
# cp.deposita(1000.0)
# ci.deposita(1500.0)

# adc = AtualizadorDeContas(0.01)

# adc.roda(cc)
# adc.roda(cp)
# adc.roda(ci)

# print(f"Saldo total acumulado: {adc.saldo_total}")
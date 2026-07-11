class Conta:
    def __init__(self, numero, titular, saldo, limite, codigo_tipo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_tipo = codigo_tipo
        if self.codigo_tipo == 1:
            self.tipo = "Conta Corrente"
        else:
            self.tipo = "Conta Poupança"

    def depositar(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if valor > self.saldo:
            return False
        self.saldo -= valor
        return True
    
    def transferir(self, valor, destino):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return False
        self.saldo -= valor
        destino.depositar(valor)
        return True
    
    def extrato(self):
        print("numero: {}\nsaldo: {}".format(self.numero, self.saldo))

banco = {}

while True:
    print("1 - Cadastro de Conta")
    print("2 - Entrar na Conta")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        numero = input("Digite o número da conta: ")
        titular = input("Digite o nome do titular: ")
        saldo = float(input("Digite o saldo inicial: "))
        limite = float(input("Digite o limite: "))
        codigo_tipo = int(input("Digite o código do tipo (1 - Conta Corrente, 2 - Conta Poupança): "))
        banco[numero] = Conta(numero, titular, saldo, limite, codigo_tipo)
        print("Conta cadastrada com sucesso!")
    elif opcao == 2:
        numero = input("Digite o número da conta: ")
        if numero not in banco:
            print("Conta não encontrada")
            continue
        conta = banco[numero]
        while True:
            print("1 - Depositar")
            print("2 - Sacar")
            print("3 - Transferir")
            print("4 - Extrato")
            print("5 - Sair")
            opcao_conta = int(input("Escolha uma opção: "))
            if opcao_conta == 1:
                valor = float(input("Digite o valor a ser depositado: "))
                conta.depositar(valor)
                print("Depósito realizado")
            elif opcao_conta == 2:
                valor = float(input("Digite o valor a ser sacado: "))
                if conta.saca(valor):
                    print("Saque realizado")
                else:
                    print("Saldo insuficiente")
            elif opcao_conta == 3:
                numero_destino = input("Digite o número da conta de destino: ")
                if numero_destino not in banco:
                    print("Conta de destino não encontrada")
                    continue
                valor = float(input("Digite o valor a ser transferido: "))
                if conta.transferir(valor, banco[numero_destino]):
                    print("Transferência realizada")
                else:
                    print("Saldo insuficiente")
            elif opcao_conta == 4:
                conta.extrato()
            elif opcao_conta == 5:
                print("Saindo da conta")
                break
            else:
                print("Opção inválida")
    elif opcao == 3:
        print("Saindo do programa")
        break
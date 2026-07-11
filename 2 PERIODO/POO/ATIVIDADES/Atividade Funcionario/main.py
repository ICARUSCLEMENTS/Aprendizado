from Funcionario import Funcionario
from Gerente import Gerente
from Vendedor import Vendedor
from ControleDeBonificacoes import ControleDeBonificacoes

# Criar os objetos Funcionario, Gerente e Vendedor
funcionario = Funcionario("João", "111111111-11", 2000)

# Implemente a criação de um objeto Gerente aqui
gerente = Gerente("Maria", "222222222-22", 5000, "senha123", 5)

# Implemente a criação de um objeto Vendedor aqui
vendedor = Vendedor("Carlos", "333333333-33", 1000, 6000, 10)

# Controle de Bonificações
controle = ControleDeBonificacoes()

# Registre os funcionários no controle
controle.registra(funcionario)
controle.registra(gerente)
controle.registra(vendedor)

# Imprima os valores das bonificações e o total
print(f"Bonificação Funcionário: {funcionario.get_bonificacao()}")
print(f"Bonificação Gerente: {gerente.get_bonificacao()}")
print(f"Bonificação Vendedor: {vendedor.get_bonificacao()}")
print(f"Total de Bonificações: {controle.total_bonificacoes}")
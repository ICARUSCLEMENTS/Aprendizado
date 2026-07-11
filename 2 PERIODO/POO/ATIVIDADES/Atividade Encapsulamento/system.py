class Veiculo:
    def __init__(self, tipo, marca, modelo, ano, peso, kmporlitro, quantidade_de_combustivel, tipode_combustivel):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.peso = peso
        self.tipode_combustivel = tipode_combustivel
        self.kmporlitro = kmporlitro
        self.quantidade_de_combustivel = quantidade_de_combustivel

    def andar(self, distancia):
        if self.quantidade_de_combustivel <= 0:
            print("O carro não pode andar, pois não há combustível.")
            return
        
        consumo = distancia / self.kmporlitro
        if consumo > self.quantidade_de_combustivel:
            print("Não há combustível suficiente para percorrer a distância.")
            return
        
        self.quantidade_de_combustivel -= consumo
        print(f"O carro andou {distancia} km. Combustível restante: {self.quantidade_de_combustivel:.2f} litros.")
    
    def mostrar_informacoes(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Peso: {self.peso} kg")
        print(f"Combustível: {self.tipode_combustivel}")
        print(f"Km por litro: {self.kmporlitro}")
        print(f"Quantidade de combustível: {self.quantidade_de_combustivel:.2f} litros")

    def mostrar_combustivel(self):
        print(f"Combustível restante: {self.quantidade_de_combustivel:.2f} litros.")

class BombadeCombustivel:
    def __init__(self, tipoCombustivel, ValorLitro, quantidadeCombustivel):
        self.__tipoCombustivel = tipoCombustivel
        self.__ValorLitro = ValorLitro
        self.__quantidadeCombustivel = quantidadeCombustivel

    def get_mostrarinformacoes(self):
        print(f"Tipo de Combustível: {self.__tipoCombustivel}")
        print(f"Valor do Litro: {self.__ValorLitro:.2f} reais")
        print(f"Quantidade de Combustível: {self.__quantidadeCombustivel:.2f} litros")

    def abastecerPorValor(self, veiculo, valor):
        if self.__tipoCombustivel != veiculo.tipode_combustivel:
            print(f"Tipo de combustível incompatível: {self.__tipoCombustivel} não é compatível com {veiculo.tipode_combustivel}.")
            return
        
        litros = valor / self.__ValorLitro
        if litros > self.__quantidadeCombustivel:
            print("Não há combustível suficiente na bomba.")
            return
        
        veiculo.quantidade_de_combustivel += litros
        self.__quantidadeCombustivel -= litros
        print(f"Abastecido {litros:.2f} litros") 

    def abastecerPorLitro(self, veiculo, litros):
        if self.__tipoCombustivel != veiculo.tipode_combustivel:
            print(f"Tipo de combustível incompatível: {self.__tipoCombustivel} não é compatível com {veiculo.tipode_combustivel}.")
            return
        
        if litros > self.__quantidadeCombustivel:
            print("Não há combustível suficiente na bomba.")
            return
        
        veiculo.quantidade_de_combustivel += litros
        self.__quantidadeCombustivel -= litros
        print(f"Abastecido {litros:.2f} litros | Valor total: {litros * self.__ValorLitro:.2f} reais")

    def set_alterarValor(self, novoValor):
        self.__ValorLitro = novoValor
        print(f"Valor do litro alterado para: {self.__ValorLitro:.2f} reais")

    def set_alterarCombustivel(self, novoCombustivel):
        self.__tipoCombustivel = novoCombustivel
        print(f"Tipo de combustível alterado para: {self.__tipoCombustivel}")
    
    def set_alterarQuantidadeCombustivel(self, novaQuantidade):
        self.__quantidadeCombustivel = novaQuantidade
        print(f"Quantidade de combustível na bomba alterada para: {self.__quantidadeCombustivel:.2f} litros")



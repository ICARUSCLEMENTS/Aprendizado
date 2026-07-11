class Veiculo:
    def mover(self):
        print("O veículo está se movendo.")

class Motorizado:
    def ligar_motor(self):
        print("Motor ligado!")

class Eletrico:
    def carregar_bateria(self):
        print("Bateria carregando...")

class Carro(Veiculo, Motorizado):
    def __init__(self, modelo):
        self.modelo = modelo

class CarroEletrico(Carro, Eletrico):
    def __init__(self, modelo):
        super().__init__(modelo)

class Bicicleta(Veiculo):
    def __init__(self, tipo):
        self.tipo = tipo


tesla = CarroEletrico("model 3")
tesla.ligar_motor()
tesla.carregar_bateria()
tesla.mover()

bike = Bicicleta("montana")
bike.mover()
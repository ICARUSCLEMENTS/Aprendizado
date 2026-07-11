class Cadeira:
    Altura_max = 80
    Altura_min = 50
    def __init__(self, modelo, fabricante, peso, carga, preco, altura):
        self.modelo = modelo
        self.Fabricante = fabricante
        self.Peso = peso
        self.Carga = carga
        self.Preco = preco
        self.Altura = altura

    def subir(self):
        if self.Altura < self.Altura_max:
            self.Altura += 5
        else:
            print("Altura máxima atingida")
    
    def descer(self):
        if self.Altura > self.Altura_min:
            self.Altura -= 5
        else:
            print("Altura mínima atingida")


# cadeira_1 = Cadeira()
# cadeira_1.Preco = 2500
# print(cadeira_1.Preco)

c1 = Cadeira()
c2 = Cadeira()
c3 = Cadeira()

print("c1 Antes " + str(c1.Preco))
c1.Preco = 1000
print("c1 Depois " + str(c1.Preco))
print("c2 " + str(c2.Preco))

print(c1.Altura)
c1.subir()
c1.subir()
c1.subir()
c1.subir()
print(c1.Altura)
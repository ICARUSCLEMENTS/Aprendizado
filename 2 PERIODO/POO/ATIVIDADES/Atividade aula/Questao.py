class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos=1):
        for i in range(anos):
            self.idade += 1
            if self.idade <= 21:
                self.altura += 0.05
    
    def engordar(self, quilos):
        self.peso += quilos
    
    def emagrecer(self, quilos):
        self.peso -= quilos
    
    def crescer(self, centimetros):
        self.altura += centimetros / 100
    

p1 = Pessoa("João", 15, 70, 1.75)

p1.envelhecer()
print(p1.idade) 
print(p1.altura)
print(p1.peso)
p1.engordar(5)
print(p1.peso)
p1.emagrecer(2)
p1.crescer(10)
print(p1.altura)
print(p1.nome)
print(p1.idade)
print(p1.peso)
print(p1.altura)
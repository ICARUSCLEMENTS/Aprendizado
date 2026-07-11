class pessoa:
    def __init__(self, nome, idade, tamanho, genero):
        self.nome = nome
        self.idade = idade
        self.__tamanho = tamanho
        self.__genero = genero

    def envelhecer(self, anos=1):
        self.idade += anos
        print(f"{self.nome} agora tem {self.idade} anos.")

    def crescer(self, centimetros):
        self.__tamanho += centimetros
        print(f"{self.nome} agora tem {self.__tamanho} cm de altura.")
    
    def set_mudarGenero(self, novoGenero):
        self.__genero = novoGenero
    
    def set_mudarTamanho(self, novoTamanho):
        self.__tamanho = novoTamanho
    
    def get_Tamanho(self):
        return self.__tamanho

    def get_Genero(self):
        return self.__genero
    
    def get_informacoes(self):
        return f"Nome: {self.nome} \nIdade: {self.idade} \nTamanho: {self.__tamanho} cm \nGênero: {self.__genero}"

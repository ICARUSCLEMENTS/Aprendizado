from abc import ABC, abstractmethod

# Interface para um atacante
class Atacante(ABC):
    @abstractmethod
    def chutar_ao_gol(self):
        pass

# Interface para um defensor
class Defensor(ABC):
    @abstractmethod
    def bloquear_chute(self):
        pass

# Interface para um meio-campista
class MeioCampista(ABC):
    @abstractmethod
    def dar_assistencia(self):
        pass

class Goleiro(ABC):
    @abstractmethod
    def defender_penalti(self):
        pass


class Jogador1(Atacante, MeioCampista):
    def chutar_ao_gol(self):
        print("Jogador1 chutou forte no gol!")

    def dar_assistencia(self):
        print("Jogador1 deu uma bela assistência!")

class Jogador2(Defensor, MeioCampista):
    def bloquear_chute(self):
        print("Jogador2 bloqueou o chute!")

    def dar_assistencia(self):
        print("Jogador2 fez um passe incrível!")

class Jogador3(Goleiro, Defensor):
    def defender_penalti(self):
        print("Jogador3 fez uma defesa espetacular!")

    def bloquear_chute(self):
        print("Jogador3 bloqueou o chute com maestria!")
    



j1 = Jogador1()
j1.chutar_ao_gol()
j1.dar_assistencia()

j2 = Jogador2()
j2.bloquear_chute()
j2.dar_assistencia()

j3 = Jogador3()
j3.defender_penalti()
j3.bloquear_chute()
from system import Veiculo
from system import BombadeCombustivel

c1 = Veiculo("Carro", "Fiat", "Uno", 2020, 800, 15, 50, "Gasolina")

bomba = BombadeCombustivel("Gasolina", 5.0, 100)

c1.andar(15)
c1.mostrar_combustivel()

bomba.abastecerPorValor(c1, 20)
c1.mostrar_combustivel()
bomba.abastecerPorLitro(c1, 5)
c1.mostrar_combustivel()
c1.mostrar_informacoes()

bomba.get_mostrarinformacoes()
bomba.set_alterarQuantidadeCombustivel(50)
bomba.set_alterarValor(6.0)
bomba.set_alterarCombustivel("Etanol")
bomba.get_mostrarinformacoes()
print(bomba.__tipoCombustivel())
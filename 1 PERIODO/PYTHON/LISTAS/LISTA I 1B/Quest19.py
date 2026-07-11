distancia = float(input("Digite a distância em Km: "))
pgasolina = float(input("Digite o preço da gasolina por litro em reais: "))
litroc = distancia / 12
gasto = litroc * pgasolina
print("O carro irá consumir ", litroc, " litros.")
print("O dinheiro gasto nessa brincadeira é R$",gasto)
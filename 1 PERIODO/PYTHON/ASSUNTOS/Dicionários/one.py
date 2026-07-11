Dic = {'Batata': 2.5, 'Banana': 4.00, 'Maçã': 3.50}
while True:
    usu = input("Digite uma fruta para saber o preço da fruta ou fim para sair: ").capitalize()
    if usu == "Fim":
        break
    Dic.append(usu)

if usu in Dic:
    print(usu)

for chave in Dic.keys():
    print(chave)

for valor in Dic.values():
    print(valor)

for chave, valor in Dic.items():
    print(f"{chave} : {valor}")
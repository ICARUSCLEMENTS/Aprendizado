tabela = {
    "Maçã": 1.50,
    "Banana": 0.80,
    "Pão": 3.00,
    "Leite": 4.50,
    "Arroz": 5.00
}

while True:
    print("Maçã: 1.50 / banana: 0.80 / pão: 3.00 / leite: 4.50 / arroz: 5.00")
    produto = str(input("Digite o nome do produto ou 'fim' para cancelar: ")).capitalize()
    quantidade = int(input("Digite a quantidade do produto ou 0 para cancelar: "))

    
    if produto == 'Fim':
        break
    if quantidade == 0:
        break
    valor_total = tabela[produto] * quantidade
print (valor_total)
print("Fim das compras")
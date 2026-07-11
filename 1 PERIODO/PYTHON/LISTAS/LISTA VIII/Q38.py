taxascambio = {
    "USD": 5.25,
    "EUR": 6.20,
    "GBP": 7.10
}

moeda = input("Digite a moeda (USD, EUR, GBP): ")
valor = float(input("Digite o valor em BRL: "))

if moeda in taxascambio:
    valorconvertido = valor / taxascambio[moeda]
    print(f"O valor convertido é: {valorconvertido:.2f} {moeda}")
else:
    print("Moeda não encontrada.")

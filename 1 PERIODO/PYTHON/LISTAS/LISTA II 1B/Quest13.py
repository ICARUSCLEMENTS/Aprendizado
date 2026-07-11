taxa = float(input("Digite o valor da taxa de câmbio: "))
dolar = float(input("Digite o quantia que queira converter: "))
conversao = dolar * taxa
print("$%.2f dólares são iguais a R$%.2f" % (dolar, conversao))
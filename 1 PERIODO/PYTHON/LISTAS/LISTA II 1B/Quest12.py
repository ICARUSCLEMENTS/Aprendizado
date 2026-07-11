valorcompra = float(input("Digite o valor da compra: "))
valorpago = float(input("Digite o valor que irá ser pago: "))
troco = valorpago - valorcompra
print("O troco é de: R$%.2f" % (troco))
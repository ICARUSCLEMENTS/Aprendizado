# Questão 5
idade = int(input("Digite sua idade: "))
compra = float(input("Digite o valor de sua compra: "))

if idade < 18:
    compra = compra * 0.90
    print("Você tem direito a 10%% de desconto, assim o valor ficará: R$ %.2f" % (compra))
elif idade >= 60:
    compra = compra * 0.80
    print("Você tem direito a 20%% de desconto, assim o valor ficará: R$ %.2f" % (compra))
else:
    print("Você não tem direito a desconto!")

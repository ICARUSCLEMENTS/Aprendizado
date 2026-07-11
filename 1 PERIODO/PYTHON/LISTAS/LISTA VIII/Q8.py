preco = float(input("Digite o preço da compra: "))

if preco > 100:
    print(f"Desconto aplicado, o preço agora é: R${preco * 0.9:.2f}")

else:
    print("Não há desconto!")
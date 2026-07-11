pprodutos = []
while True:
    preco = input("Digite um preço ou 'sair' para finalizar: ")
    if preco.lower() == 'sair':
        break
    else:
        try:
            pprodutos.append(float(preco))
        except ValueError:
            print("Por favor, digite um número válido.")
desconto = int(input("Quanto é o desconto: "))
soma = sum(pprodutos)
pdesconto = soma * (1 - desconto / 100)
if desconto <= 0:
    print("O preço total é R$",soma)
else: 
    print("O preço total é R$",soma)
    print("O preço após o desconto é", pdesconto)
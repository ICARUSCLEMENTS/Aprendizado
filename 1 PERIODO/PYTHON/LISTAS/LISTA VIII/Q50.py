estoque = {}

while True:
    ação = input("Deseja 'adicionar', 'remover', 'consultar' ou 'sair'? ").lower()
    if ação == 'sair':
        break
    produto = input("Digite o nome do produto: ")
    
    if ação == 'adicionar':
        quantidade = int(input("Digite a quantidade: "))
        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade
    elif ação == 'remover':
        if produto in estoque:
            quantidade = int(input("Digite a quantidade a remover: "))
            if quantidade >= estoque[produto]:
                del estoque[produto]
            else:
                estoque[produto] -= quantidade
        else:
            print("Produto não encontrado.")
    elif ação == 'consultar':
        if produto in estoque:
            print(f"{produto}: {estoque[produto]}")
        else:
            print("Produto não encontrado.")
    else:
        print("Ação inválida.")

print("Estoque final:", estoque)

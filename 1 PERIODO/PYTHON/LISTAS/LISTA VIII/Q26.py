nome = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
remover = input("Digite o nome que você quer remover: ")

if remover in nome:
    nome.remove(remover)
else:
    print(f"O nome {remover} não foi encontrado na lista.")

print("Lista atualizada:", nome)
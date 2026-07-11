agenda = {
    "Ana": "1234-5678",
    "Bruno": "2345-6789",
    "Carlos": "3456-7890"
}

nomecontato = input("Digite o nome do contato: ")

if nomecontato in agenda:
    print(f"O telefone de {nomecontato} é {agenda[nomecontato]}")
else:
    print(f"Contato {nomecontato} não encontrado.")

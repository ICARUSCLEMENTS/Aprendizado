aluno = {"nome" : "Ana", "idade" : "19"}

while True:
    aluno = input("Digite para adicionar ou fim para finalizar: ").lower()
    ad = input("Digite um valor para o que você quer adicionar: ")
    if ad == "fim":
        break
    aluno[ad] = "fgfg"
Dic = {
    "nome": "Ícaro", "idade" : 15, "cidade": "Almino-Afonso"
}

while True:
    bu = input("Digite oque quer saber ou fim para finalizar: ").lower()
    if bu == "fim":
        break
    if bu in Dic:
        print(Dic[bu])
    else:
        print("Procure por cidade, idade ou nome!")
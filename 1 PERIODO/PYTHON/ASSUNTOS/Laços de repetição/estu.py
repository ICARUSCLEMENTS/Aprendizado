nomedeusuario = "Icaro123"
senha = "trigershot"

while True:
    nomeespe = input("Username: ")
    senhaespe = input("Password: ")
    if nomeespe == senhaespe:
        print("A senha não pode ser igual ao nome de usuário!")
    elif nomeespe != nomedeusuario:
        print("Usuário não encontrado!")
    elif senhaespe != senha:
        print("Senha incorreta!")
    else:
        print("Logado com sucesso!")
        break
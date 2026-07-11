numero = []
nome = []
while True:
    print("1 - Cadastrar Número")
    print("2 - Buscar Número")
    print("3 - Sair")

    cadastrador = int(input("Digite o número da opção escolhida: "))

    if cadastrador == 1:
        digitar_numero = input("Digite o número: ")
        digitar_nome = input("Digite um nome para o número: ")
        numero.append(digitar_numero)
        nome.append(digitar_nome)
        print("Cadastrado!")
    elif cadastrador == 2:
        buscar = input("Qual contato você deseja procurar?: ")
        if buscar in nome:
            buscador = nome.index(buscar)
            print(numero[nome.index(buscar)])
    elif cadastrador == 3:
        print("Protótipo finalizado")
        break

while True:
    nome = input("Digite seu nome ou digite 'sair': ")
    if nome.lower() == 'sair':
        print("Finalizado")
        break
    saltos = []
    contador = 0
    while contador < 5:
        contador += 1
        salto = float(input("Digite a distância: "))
        saltos.append(salto)
    
    print(f"Atleta - {nome}")

    print(" ")

    print(f"Primeiro salto: {saltos[0]}m")
    print(f"Segundo salto: {saltos[1]}m")
    print(f"Terceiro salto: {saltos[2]}m")
    print(f"Quarto salto: {saltos[3]}m")
    print(f"Quinto salto: {saltos[4]}m")
    print(f"Maior salto: {max(saltos)}")
    print(f"Menor salto: {min(saltos)}")
    saltos.pop(saltos.index(max(saltos)))
    saltos.pop(saltos.index(min(saltos)))
    print(f"Média das demais distâncias: {sum(saltos)/len(saltos)}")

    print(" ")

    print(f"Resultado Final: {nome} - {sum(saltos)/len(saltos)}")
while True:
    fato = int(input("Digite o número para saber o fatorial ou '0' para finalizar: "))
    ft = fato
    fatorial = 0
    contador = 0

    if fato > 0:
        while contador < ft:
            contador += 1
            if fatorial <= fato :
                fatorial +=1
                fato *= ft - 1
                ft -= 1
        print(fato)
    elif fato == 0:
        print("Programa finalizado.")
        break
    else:
        print("Digite um número positivo!")
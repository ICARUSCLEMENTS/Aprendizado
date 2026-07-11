soma = 0

while True:
    num = int(input("Digite um número ou '-1' para sair: "))
    if num == -1:
        print(soma)
        break
    soma += num
    print(soma)
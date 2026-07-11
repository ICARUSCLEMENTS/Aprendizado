lista = [5, 10, 15, 20, 25]

while True:
    numero = int(input("Digite o número(ou 0 para sair): "))
    
    if numero in lista:
        print(f"O número {numero} está na lista.")
    else:
        print(f"O número {numero} não está na lista.")
    if numero == 0:
        break
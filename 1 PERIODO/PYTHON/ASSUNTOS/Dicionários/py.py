contador = 1
while True:
    tab = int(input('Digite um número para saber a tabuada(ou 0 para finalizar o programa): '))
    if tab == 0:
        break
    while contador <= 10:
        print(f'{tab} x {contador} = {tab * contador}')
        contador += 1
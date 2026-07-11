contador = 0
soma = 0

while True:
    contador += 1
    try:
        notasme = float(input("Digite a nota(0-10): "))
        if notasme < 0 or notasme > 10:
            contador -= 1
            break
    except ValueError:
            contador -= 1
            break
    
    soma += notasme

if contador == 0:
    print("Não há como calcular a média")
else:
    print("Média da turma é: %.1f" % (soma/contador))
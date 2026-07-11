# Questão 16
inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

if inicio > fim:
    inicio, fim = fim, inicio

num = inicio
while num <= fim:
    if num > 1:
        primo = True
        i = 2
        while i <= num // 2:
            if num % i == 0:
                primo = False
                break
            i += 1
        if primo:
            print(num)
    num += 1
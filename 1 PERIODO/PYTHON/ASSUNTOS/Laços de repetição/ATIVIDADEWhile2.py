snumeros = []

while True:
    somanum = input("Digite um número ou digite '0' para somar todos os números digitados: ")
    if somanum == '0':
        break
    else:
        try:
            snumeros.append(float(somanum))
        except ValueError:
            print("Por favor, digite um número válido!")

soma = sum(snumeros)
print("A soma dos números é: %.1f" % soma)
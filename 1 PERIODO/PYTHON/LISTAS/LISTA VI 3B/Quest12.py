# Questão 12
contador_negativos = 0

while True:
    numero = int(input("Digite um número ou '0' para terminar: "))
    if numero == 0:
        break
    elif numero < 0:
        contador_negativos += 1

print(f"Você inseriu {contador_negativos} número(s) negativo(s).")
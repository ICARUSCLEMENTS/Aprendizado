# Questão 13
primeiro_numero = int(input("Digite um número ou '0' para terminar: "))
maior_numero = primeiro_numero

while primeiro_numero != 0:
    numero = int(input("Digite um número ou '0' para terminar: "))
    if numero == 0:
        break
    if numero > maior_numero:
        maior_numero = numero


print(f"O maior número inserido foi: {maior_numero}")
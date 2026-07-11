# Questão 10
soma = 0
quantidade = 0

while True:
    nota = input("Digite uma nota de 0 a 10 ou 'S' para sair: ")
    if nota.upper() == 'S':
        break
    nota = float(nota)
    if 0 <= nota <= 10:
        soma += nota
        quantidade += 1
    else:
        print("Nota inválida. Digite uma nota de 0 a 10.")

if quantidade > 0:
    media = soma / quantidade
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi digitada.")
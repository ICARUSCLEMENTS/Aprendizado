texto = input("Digite um texto: ")
vogais = "aeiouAEIOU"
contagem_vogais = 0

for char in texto:
    if char in vogais:
        contagem_vogais += 1

print(f"O texto possui {contagem_vogais} vogais.")

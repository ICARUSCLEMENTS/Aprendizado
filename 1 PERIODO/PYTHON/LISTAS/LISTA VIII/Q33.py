frase = input("Digite uma frase: ")
palavras = frase.split()
ocorrencias = {}

for palavra in palavras:
    if palavra in ocorrencias:
        ocorrencias[palavra] += 1
    else:
        ocorrencias[palavra] = 1

for palavra, contagem in ocorrencias.items():
    print(f"A palavra '{palavra}' aparece {contagem} vezes.")

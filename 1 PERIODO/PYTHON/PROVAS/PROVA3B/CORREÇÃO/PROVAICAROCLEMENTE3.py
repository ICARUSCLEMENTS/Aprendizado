numint = int(input("Digite um número para saber a tabuada: "))
contador = 0

while contador < 10:
    contador += 1
    print(f"{numint} x {contador}: {numint * contador}")
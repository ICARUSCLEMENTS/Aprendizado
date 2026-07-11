# Questão 7
med = float(input("Digite a primeira medida: "))
med2 = float(input("Digite a segunda medida: "))
med3 = float(input("Digite a terceira medida: "))

if med == med2 == med3:
    print("Essas medidas são de um triângulo equilátero!")
elif med == med2 or med == med3 or med2 == med3:
    print("É um triângulo isósceles!")
else:
    print("É um triângulo escaleno!")
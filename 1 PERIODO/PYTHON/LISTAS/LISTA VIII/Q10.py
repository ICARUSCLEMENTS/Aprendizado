med = float(input("Digite a primeira medida: "))
med2 = float(input("Digite a segunda medida: "))
med3 = float(input("Digite a terceira medida: "))

if med == med2 == med3:
    print("Triângulo equilátero!")
elif med == med2 or med == med3 or med2 == med3:
    print("Triângulo isósceles!")
else:
    print("Triângulo escaleno!")
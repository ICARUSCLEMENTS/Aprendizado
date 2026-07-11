temp = int(input("Digite a temperatura: "))

if temp < 0:
    print("Muito frio")
elif temp <= 10:
    print("Frio")
elif temp <= 25:
    print("Agradável")
elif temp <= 35:
    print("Quente")
else:
    print("Muito quente")
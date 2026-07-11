temperatura = []

while True:
    try:
        temp = float(input("Digite a temperatura ou digite alguma letra para finalizar: "))
        temperatura.append(temp)
    except ValueError:
        print("Finalizado")
        break

for i in temperatura:
    print(i)
print(f"A media é: {sum(temperatura)/len(temperatura)} | Maior: {max(temperatura)} | Menor: {min(temperatura)}")
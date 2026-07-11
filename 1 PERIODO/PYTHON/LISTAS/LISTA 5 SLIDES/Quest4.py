a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

if ((a and b) % 3 == 0) or ((a or b) % 5 == 0):
    print("Condição satisfeita.")
else:
    print("Condição não satisfeita.")
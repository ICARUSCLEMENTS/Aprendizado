numero1 = float(input("Digite o primeiro número real: "))
numero2 = float(input("Digite o segundo número real: "))
soma = numero1 + numero2
produto = numero1 * numero2
if numero2 != 0:
    quociente = numero1 / numero2
else:
    quociente = "Indefinido"
print("A soma dos números é:", soma)
print("O produto dos números é:", produto)
print("O quociente dos números é:", quociente)
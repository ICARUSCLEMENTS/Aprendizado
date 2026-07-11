salario = float(input("Digite seu salário: "))
imposto = 0

if salario > 3000:
    imposto = salario * 0.35


if salario > 1000:
    imposto = salario * 0.20


print(f"Salário bruto: R${salario:.2f}")
print("Salário líquido: R$%.2f" % (salario - imposto))


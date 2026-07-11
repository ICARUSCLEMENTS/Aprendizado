salario = float(input("Digite seu salário: "))
base = salario
imposto = 0

if base > 3000:
    imposto = salario * 0.35
    base = 0

if base > 1000:
    imposto = salario * 0.15

salario_liquido = salario - imposto
print(f"Salário Líquido: {salario_liquido}")
print(f"Imposto: {imposto}")
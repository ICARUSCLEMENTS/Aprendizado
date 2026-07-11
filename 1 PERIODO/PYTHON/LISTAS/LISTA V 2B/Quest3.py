# Questão 3
num = float(input("Digite o primeiro número: "))
ope = input("Digite o operador da equação: ")
num2 = float(input("Digite o segundo número: "))

if ope == "+":
    resul = num + num2
    print(f"Resultado: {resul}")
elif ope == "-":
    resul = num - num2
    print(f"Resultado: {resul}")
elif ope == "*":
    resul = num * num2
    print(f"Resultado: {resul}")
elif ope == "/":
    resul = num / num2
    print(f"Resultado: {resul}")
else:
    print("ERRO! Operador iNvÁlIdO")

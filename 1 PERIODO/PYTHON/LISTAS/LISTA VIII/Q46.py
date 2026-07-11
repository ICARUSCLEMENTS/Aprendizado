banco = {
    "Saldo": 1000,
    "Transações": []
}

while True:
    ação = input("Deseja 'depositar', 'sacar' ou 'sair'? ").lower()
    if ação == 'sair':
        break
    valor = float(input("Digite o valor: "))
    if ação == 'depositar':
        banco["Saldo"] += valor
        banco["Transações"].append(f"Depósito: {valor}")
    elif ação == 'sacar':
        if valor <= banco["Saldo"]:
            banco["Saldo"] -= valor
            banco["Transações"].append(f"Saque: {valor}")
        else:
            print("Saldo insuficiente.")
    else:
        print("Ação inválida.")

print(f"Saldo final: {banco['Saldo']}")
print("Histórico de transações:", banco["Transações"])

# Questão 17
while True:
    valor_saque = int(input("Digite o valor do saque ou '0' para sair: "))
    
    if valor_saque == 0:
        break
    
    if valor_saque < 0:
        print("Valor inválido! Tente novamente.")
        continue
    
    notas_100 = valor_saque // 100
    valor_saque %= 100
    
    notas_50 = valor_saque // 50
    valor_saque %= 50
    
    notas_20 = valor_saque // 20
    valor_saque %= 20
    
    notas_10 = valor_saque // 10
    valor_saque %= 10
    
    notas_5 = valor_saque // 5
    valor_saque %= 5
    
    print(f"Notas de 100: {notas_100}")
    print(f"Notas de 50: {notas_50}")
    print(f"Notas de 20: {notas_20}")
    print(f"Notas de 10: {notas_10}")
    print(f"Notas de 5: {notas_5}")
    print(f"Valor restante que não pode ser sacado: {valor_saque}")

print("Encerrando o programa.")
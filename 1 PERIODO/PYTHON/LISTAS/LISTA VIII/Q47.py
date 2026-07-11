nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduardo", "Amanda"]
agrupados = {}

for nome in nomes:
    inicial = nome[0].upper()
    if inicial not in agrupados:
        agrupados[inicial] = []
    agrupados[inicial].append(nome)

for inicial, lista in agrupados.items():
    print(f"{inicial}: {', '.join(lista)}")

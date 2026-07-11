
produtos = {
    "Frutas": ["Maçã", "Banana", "Laranja"],
    "Vegetais": ["Cenoura", "Alface", "Tomate"],
    "Laticínios": ["Leite", "Queijo", "Iogurte"]
}

for categoria, itens in produtos.items():
    print(f"{categoria}: {', '.join(itens)}")

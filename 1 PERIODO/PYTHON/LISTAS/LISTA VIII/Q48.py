notas_alunos = {
    "Ana": 7.5,
    "Bruno": 4.0,
    "Carlos": 6.0,
    "Daniela": 9.0,
    "Eduardo": 5.5
}

for nome, nota in notas_alunos.items():
    status = "Aprovado" if nota >= 6.0 else "Reprovado"
    print(f"{nome}: {status}")
from system import pessoa

p1 = pessoa("João", 20, 180, "Masculino")

print(p1.get_informacoes())
p1.envelhecer(5)
p1.crescer(10)
print(p1.get_informacoes())

p1.set_mudarGenero("Feminino")
print(f"Gênero: {p1.get_Genero()}")
p1.set_mudarTamanho(185)
print(f"Tamanho: {p1.get_Tamanho()}cm")

print(p1.get_informacoes())

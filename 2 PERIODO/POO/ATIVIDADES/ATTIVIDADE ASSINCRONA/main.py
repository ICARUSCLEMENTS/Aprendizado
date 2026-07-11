from classes import Vendedor

v1 = Vendedor("Ana")
v1.vendeu(800)

print(v1.bateu_meta(700))
print(v1.bonus(700))

v2 = Vendedor("Bruno")
v2.vendeu(400)

print(v2.bateu_meta(700))
print(v2.bonus(700))

v3 = Vendedor("Carlos")
v3.vendeu(1000)

print(v3.bateu_meta(700))
print(v3.bonus(700))
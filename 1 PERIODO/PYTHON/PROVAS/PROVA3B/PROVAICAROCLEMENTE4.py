primnum = int(input("Digite um número menor: "))
seconum = int(input("Digite um número maior: "))

while seconum >= primnum:
    if primnum % 2 != 0:
        print(primnum)
    primnum += 1

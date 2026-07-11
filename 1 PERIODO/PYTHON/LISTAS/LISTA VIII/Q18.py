num = int(input("Digite um número: "))

if num <= 1:
    print("Número 1 ou menor, não é primo")
else:
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            print(f"{num} não é primo")
            break
        divisor += 1
    else:
        print(f"{num} é primo")
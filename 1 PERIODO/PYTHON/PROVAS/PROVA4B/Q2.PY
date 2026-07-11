def fatorial(a):
    if a == 0:
        return 1
    resultado = 1
    for i in range(1, a + 1):
        resultado *= i

    return resultado


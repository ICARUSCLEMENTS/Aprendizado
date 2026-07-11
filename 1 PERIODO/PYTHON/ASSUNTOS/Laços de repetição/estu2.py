paisa = 80000
popub = 200000
contadoranos = 0

while paisa <= popub:
    calca = paisa * 0.03
    paisa += calca
    calcb = popub * 0.015
    popub += calcb
    contadoranos += 1

print("A contagem de anos até ultrapassar é de", contadoranos, "anos")
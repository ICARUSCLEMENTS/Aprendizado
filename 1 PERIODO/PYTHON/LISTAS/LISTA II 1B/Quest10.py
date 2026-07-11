hora = int(input("Digite a hora (Ex: 00 a 23): "))
minuto = int(input("Digite os minutos (Ex: 00 a 59): "))
minutos = 60 * hora
somamin = minutos + minuto
print("Hora Digitada - %d:%d | Em minutos %d" % (hora, minuto, somamin))

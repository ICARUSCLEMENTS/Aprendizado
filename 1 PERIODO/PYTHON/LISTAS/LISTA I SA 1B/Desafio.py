# Desafio - Questão 4
from datetime import datetime
data = datetime.now()
Dias = data.strftime("%d/%m/%Y")
horas = data.strftime("%H:%M")
import os
nome_usuario = os.getlogin()
print ("Olá " + nome_usuario + "! Hoje é " + Dias + ". E são " + horas + ".")
# -Icaro Clemente da Silva
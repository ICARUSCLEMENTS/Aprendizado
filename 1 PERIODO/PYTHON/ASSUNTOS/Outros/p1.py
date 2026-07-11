from datetime import datetime
data = datetime.now()
horas = data.strftime("%H:%M")
import os
nome_usuario = os.getlogin()
print ("Olá " + nome_usuario + "!, são " + horas + " horas.")
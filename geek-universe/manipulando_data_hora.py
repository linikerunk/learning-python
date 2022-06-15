"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

replace para alterar 5 min depois para enviar e-mail
"""

import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Ele retorna a data e hora atual
print(datetime.datetime.now())  # 2020-04-16 05:18:03.135816
print(repr(datetime.datetime.now())) # (year, month, day, hour, minute, second, microsecond)

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterando o horário para 16 horas, 0 minutos, 0 segundos, 0 microsegundo

inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)
print(inicio)

evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))
print(type('31/12/2018'))
print(evento)

nascimento = input("Informa sua data de nascimento (dd/mm/yyyy) : ")
print(nascimento)
print(type(nascimento))

nascimento = nascimento.split('/')
print(nascimento)
print(type(nascimento))

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)
print(type(nascimento))

# Acessa individual dos elementos de data e hora

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)
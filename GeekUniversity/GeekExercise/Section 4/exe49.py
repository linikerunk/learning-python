"""
Faça um programa para leia o horário ( hora, minuto e segundo) de inicio e a duração, 
em segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto e segundo) do termino da mesma.
"""
from datetime import datetime, time
import datetime

datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
date1 = input('Digite o hórario do inicio : ')
date2 = input('Digite o hórario do fim : ')
diff = datetime.datetime.strptime(date1, datetimeFormat)\
    - datetime.datetime.strptime(date2, datetimeFormat)
 
print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)
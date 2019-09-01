#Escreva um programa que leia a quantidade de dias,
#horas, minutos e segundo do usuário. Calcule o total em segundos.

qnt_dias = int(input('Digite a quantidades de dias : '))
qnt_horas = float(input('Digite a quantidades de horas:'))
qnt_minutos = float(input('Digite a quantidades de minutos: '))
qnt_segundos = float(input('Digite a quantidades de segundos: '))

qnt_minutos = float(qnt_minutos * 60)
qnt_horas = float(qnt_horas * 3600)
qnt_dias = float(qnt_dias * 3600 * 24)
total_seg = qnt_dias + qnt_horas + qnt_minutos + qnt_segundos

print(f'Os valores somados em segundos tem um total de {total_seg} segundos.')
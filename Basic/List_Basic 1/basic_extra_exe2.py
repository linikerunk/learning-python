#Escreva um programa que leia um valor em metros
#e o exiba convertido em milímetros.

metros = float(input('Digite o valor em Metros para ser convertido Milímetros : '))

conversao = (metros * 1000)

print(f'O valor {metros} convertido para milímetros é : {conversao:.2f}')
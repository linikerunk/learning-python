#Escreva um programa que pergunte o salário do funcionário e calcule o valor
#do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, de 15%.


salario = float(input('Qual o sálario do funcionário : '))

if salario > 1.250:
    aumento = salario * 0.15
    salario_aumento = salario + aumento
    print(f' Seu salário com 15% de aumento é : {salario_aumento}')
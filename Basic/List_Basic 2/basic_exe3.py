#Escreva um programa que leia dois valores inteiros
#distintos e informe qual é o maior. 

numero1 = int(input('Digite o primeiro número : '))
numero2 = int(input('Digite o segundo número : '))

if numero1 > numero2:
    print(f'O {numero1} é maior que {numero2}')
elif numero1 == numero2:
    print('Os Números digitados são')
else:
    print(f'O número {numero2} é maior que {numero1}')


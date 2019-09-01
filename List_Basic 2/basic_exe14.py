#Faça um programa que leia três números e mostre o maior e o menor deles.

numero1 = float(input('Digite o primeiro número:'))
numero2 = float(input('Digite o segundo número:'))
numero3 = float(input('Digite o terceiro número:'))

if numero1 > numero2 and numero1 > numero3 and numero2 < numero3:
    print(f'O Maior número é : {numero1}')
    print(f'O Menor número é : {numero2}')

elif numero1 > numero2 and numero1 > numero3 and numero3 < numero2:
    print(f'O Maior número é : {numero1}')
    print(f'O Menor número é : {numero3}')

elif numero2 > numero1 and numero2 > numero3 and numero1 < numero3:
    print(f'O Maior número é : {numero2}')
    print(f'O Menor número é : {numero1}')

elif numero2 > numero1 and numero2 > numero3 and numero3 < numero1:
    print(f'O Menor número é : {numero2}')
    print(f'O Menor número é : {numero3}')

elif numero3 > numero1 and numero3 > numero2 and numero1 < numero2:
    print(f'O Maior número é : {numero3}')
    print(f'O Menor número é : {numero1}')

elif numero3 > numero1 and numero3 > numero2 and numero2 < numero3:
    print(f'O Maior número é : {numero3}')
    print(f'O Menor número é : {numero2}')

elif numero3 == numero1 and numero3 > numero2:
    print(f'Maiores números são o n1 e n3 : {numero1}, {numero3}')
    print(f'Menor número é o n2 : {numero2}')

elif numero2 == numero1 and numero2 > numero3:
    print(f'Maiores números são o n2 e n1 : {numero2}, {numero1}')
    print(f'Menor número é o n3 : {numero3}')

elif numero2 == numero3 and numero2 > numero1:
    print(f'Maiores números são o n2 e n3 : {numero2}, {numero3}')
    print(f'Menor número é o n1 : {numero1}')

elif numero3 == numero1 and numero3 < numero2:
    print(f'Maior número é o {numero2}')
    print(f'Menores números são os {numero1}, {numero3}')

elif numero2 == numero1 and numero2 < numero3:
    print(f'Maior número é o {numero3}')
    print(f'Menores números são os {numero1}, {numero2}')

elif numero3 == numero2 and numero3 < numero1:
    print(f'Maior número é o {numero1}')
    print(f'Menores números são os {numero3}, {numero2}')

elif numero1 == numero2 and numero1 == numero3:
    print(f'Todos números são iguais: {numero1}')

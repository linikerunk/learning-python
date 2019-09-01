#Desenvolva um programa que solicite dois números inteiros, mostre a soma destes 
#números, e avise se a soma é maior, menor ou igual a 1000.

numero1 = float(input('Digite o número 1 : '))
numero2 = float(input('Digite o número 2 : '))
soma_numeros = numero1 + numero2
if soma_numeros >= 1000: print(f'Essa soma é maior que 1000,  Resultado da soma = {soma_numeros:.2f}')
else: print(f'Essa soma é menor que 1000,  Resultado da soma = {soma_numeros:.2f}') 

    
"""
Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o 
de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 100000.
"""

number = input("Digite um número inteiro : ")
try:
    number = int(number)
except:
    print("Digito inválido.")

cont = 0
step = 1000
for cont in range(0, 100001, step + number):
    print(cont)
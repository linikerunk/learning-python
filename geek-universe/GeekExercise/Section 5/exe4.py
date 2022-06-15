"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    * O número digitado ao quadrado.
    * A raiz quadrada do número digitado.
"""
import math

while True:
    numero = input("Digite um número : ")

    try:
        numero = float(numero)
    except:
        print("O valor precisa ser um número.")
    if numero >= 0:
        raiz = math.sqrt(numero)
        potencia = numero ** 2
        print(f"Raiz de {numero} : {round(raiz, 2)}")
        print(f'Elevado ao quadrado de {numero}  : {round(potencia, 2)}')
    else:
        print(f"{numero} é um número negativo.")

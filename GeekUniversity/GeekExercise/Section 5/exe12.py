"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número
Inválido". Se o número for positivo, calcular o logaritmo deste número.
"""

import math

while True:
    number = input("Digite um número : ")
    try:
        number = float(number)
    except:
        print("Digito inválido.")
    finally:
        print(f'O logaritmo desse número é : {round(math.log2(number), 2)} ')

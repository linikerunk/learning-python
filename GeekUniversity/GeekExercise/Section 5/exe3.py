"""
Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o numero ao quadrado
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
        print(f"A raiz quadrada do número {numero} é {round(raiz, 2)}")
    else:
        potencia = numero ** 2
        print(f'O número {numero} elevado ao quadrado é : {round(potencia, 2)}')
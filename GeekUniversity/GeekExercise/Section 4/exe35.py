"""
Sejam a e b catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = Raiz a² + b². Faça um programa que receba os valores de a e b
calcule o  valor da hipotenusa através da equação, Imprima o resultado dessa
operação.

"""

import math

while True:
    try:
        cateto_a = input("Digite o valor do primeiro cateto : ")
        cateto_b = input("Digite o valor do segundo cateto :")

        cateto_a, cateto_b = float(cateto_a), float(cateto_b)
        # print(type(cateto_a), type(cateto_b))
        hipotenusa = (math.sqrt(cateto_a ** 2 + cateto_b ** 2))
        print(f" O valor da Hipotenusa é : {round(hipotenusa, 2)}")
    except:
        print("Teste")
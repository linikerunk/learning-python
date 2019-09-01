#Faça um programa que calcule e mostre a área de um círculo.

import math

raio = float(input(f'Digite a raio do seu círculo: '))
A = (math.pi * raio ** 2)
print(f'A área do seu círculo é : {A:.2f}')
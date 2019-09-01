# Elabore um programa que efetue a leitura de três valores inteiros (A, B e C)
# e apresente como resultado a soma dos quadrados dos três valores lidos. 

import math

A = float(input('Digite o valor de A : '))
B = float(input('Digite o valor de B : '))
C = float(input('Digite o valor de C : '))

A = pow(A, 2)
B = pow(B, 2)
C = pow(C, 2)

soma_quad = (A + B + C)
print(f"Resultado da soma dos quadrados dos três valores : {soma_quad:.2f}")
"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
O volume de um cilindro circular é calculado por meio da seguinte fórmula
V = PI *  raio² * altura, onde PI = 3.141592.
"""

PI = 3.141592

altura = input("Digite a altura do cilindro : ")
raio = input("Digite o valor do raio do cilindro : ")

###############################################################################
try:
    altura, raio = float(altura), float(raio)
    cilindro = altura *  (raio**2) * PI
    print(f" O Volume do cilindro é igual a : {cilindro}")
except:
    print("Valor inválido")
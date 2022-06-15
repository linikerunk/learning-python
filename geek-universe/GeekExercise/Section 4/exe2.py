"""
Faça um programa que leia um número real e o imprima.
"""

while True:
    numero = input("Digite um número:")
    try:
        numero = float(numero)
        break
    except:
        print("numero não é um número real..")

print(f"Número digitado : {numero}")
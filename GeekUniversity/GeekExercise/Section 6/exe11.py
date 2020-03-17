"""
Faça um programa que leia um número inteiro positivo N e imprima todos os nú-
meros naturais de 0 ate N em ordem crescente.
"""

number = input("Digite um número inteiro : ")
try:
    number = int(number)
except:
    print("Digito inválido")
finally:
    for show in range(0, number+1, 1):
        print(show)
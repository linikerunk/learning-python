"""
Faça um programa que some todos os números naturais abaixo de 1000 que são múlti
plos de 3 ou 5 
"""

for num in range(0, 1001):
    if num % 3 == 0 or num % 5 == 0:
        print(num)
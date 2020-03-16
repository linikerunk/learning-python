"""
Faça um programa que determine o mostre os cinco primeiros múltiplos de 3, consi
derando números maiores que 0.
"""

print("5 primeiros números múltiplos de 3 : \n")
for number in range(1, 16):
    if number % 3 == 0:
        print("Número : ", number)
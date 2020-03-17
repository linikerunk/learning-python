"""
Faça um programa que leia 10 inteiros e imprima sua média.
"""

for number in range(0, 10):
    number = input("Digite um número inteiro : ")
    try:
        number = int(number)
    except:
        print("Digito inválido.")
    sum_of_number += number

average = sum_of_number / 10
print(f"A média dos números é : {round(average, 2)}")
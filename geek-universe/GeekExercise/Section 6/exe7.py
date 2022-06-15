"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e 
imprima sua média.
"""

sum_of_number = 0
cont = 0
while cont <= 10:
    number = input("Digite um número : ")
    try:
        number = int(number)
    except:
        print("Digite um número válido.")
    finally:
        if number < 0:
            cont = cont - 1
            cont = cont + 1
        else:
            sum_of_number += number
            cont = cont + 1

average = (sum_of_number / 10) 
print(f"A média dos 10 números positivos é igual a : {average}")
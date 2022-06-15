"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros
números naturais ímpares.
"""

while True:
    number = input("Digite um número : ")
    counter = 0
    try:
        number = int(number)
    except:
        print("Digito inválido.")
    finally:
        while counter <= number:
            if counter % 2 == 1:
                print(counter)
            counter = counter + 1
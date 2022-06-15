"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
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
            if counter % 2 == 0:
                print(counter)
            counter = counter + 1
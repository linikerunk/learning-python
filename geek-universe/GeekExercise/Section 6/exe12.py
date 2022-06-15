"""
Faça um programa que leia um npumero inteiro positivo N e imprima todos os núme-
ros naturais de 0 até N em ordem decrescente.
"""

while True:
    numbers = []
    number = input("Digite um número inteiro : ")
    try:
        number = int(number)
    except:
        print("Digito inválido")
    finally:
        if number < 0:
            print("Digito inválido, precisa ser um número positivo.")
        else:
            for show in range(0, number+1, 1):
                numbers.append(show)
    print(list(reversed(numbers)))
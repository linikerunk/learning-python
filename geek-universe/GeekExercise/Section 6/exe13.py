"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os
números pares de 0 até N em ordem crescente
"""

while True:
    numbers = []
    number = input("Digite um número inteiro : ")
    try:
        number = int(number)
    except:
        print("Digito inválido")
    finally:
        if number % 2 != 0:
            print("Digito inválido, precisa ser um número par.")
            break
        else:
            for show in range(0, number+1, 1):
                if show % 2 != 0:
                    pass
                else:
                    numbers.append(show)
    print(list(numbers))
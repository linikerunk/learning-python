"""
Faça um programa que leia um número inteiro positivo impar N e imprima todos 
números impares de 1 até N em ordem crescente.
"""
while True:
    numbers = []
    number = input("Digite um número inteiro : ")
    try:
        number = int(number)
    except:
        print("Digito inválido")
    finally:
        if number % 2 != 1:
            print("Digito inválido, precisa ser um número impar.")
            break
        else:
            for show in range(0, number+1, 1):
                if show % 2 != 1:
                    pass
                else:
                    numbers.append(show)
    print(list(numbers))

"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem Números iguais.
"""

while True:
    first_number = input("Digite o primeiro número : ")
    second_number = input("Digite o segundo número : ")
    try:
        first_number, second_number = float(first_number), float(second_number)
    except:
        print("Digito inválido.")
    finally:
        if first_number > second_number:
            diff = first_number - second_number
            print(f"Entre {second_number} e {first_number} o [{first_number} É O MAIOR].")
            print(f"A diferença entre eles é igual a {round(diff, 2)}.")
        elif second_number > first_number:
            diff = second_number - first_number
            print(f"Entre {second_number} e {first_number} [{second_number} É O MAIOR].")
            print(f"A diferença entre eles é igual a {round(diff, 2)}.")
        else:
            print("Os números são iguais.")
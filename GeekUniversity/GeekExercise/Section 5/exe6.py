"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior 
deles assim como a diferença existente entre ambos.
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
        else:
            diff = second_number - first_number
            print(f"Entre {second_number} e {first_number} [{second_number} É O MAIOR].")
            print(f"A diferença entre eles é igual a {round(diff, 2)}.")
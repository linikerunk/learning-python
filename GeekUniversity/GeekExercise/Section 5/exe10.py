"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre 
seu peso ideal, utilizando as seguintes fórmulas ( onde H corresponde à altura):
    * Homens (72.7 * H) - 58
    * Mulheres (62.1 * H) - 44,7
"""

while True:
    gender = input("Digite o sexo da pessoa : ")
    height = input("Digite a altura da pessoa : ")

    try:
        gender, height = str(gender.upper()), float(height)
    except:
        print("Digito inválido.")
    finally:
        if gender == "F":
            body_mass = (62.1 * height) - 44.7
            print(f"Seu peso ideal é : {round(body_mass, 2)}")
        elif gender == "M":
            body_mass = (72.7 * height) - 58
            print(f"Seu peso ideal é : {round(body_mass, 2)}")
        else:
            print("Opção inválida.")

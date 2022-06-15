"""
Faça um programa que calcule e mostre área de um trapézio. Sabe-se qye:
    A = ((basemaior + basemenor) * altura) / 2
Lembre-se que a base maior e a base menor devem ser números maiores que zero
"""

while True:
    large_base = input("Digite o valor da Base Maior : ")
    smaller_base = input("Digite o valor da Base Menor : ")
    height = input("Digite a altura do trapézio : ")

    try:
        large_base, smaller_base, height = float(large_base), float(smaller_base), float(height)
    except:
        print("Digito inválido.")
    finally:
        if large_base <= 0 or smaller_base <= 0:
            print("As bases não podem ser negativas.")
        else:
            area = ((large_base + smaller_base) * height) / 2
            print(f"À area do trapézio é : {round(area, 2)}")
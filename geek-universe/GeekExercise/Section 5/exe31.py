"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a
tabela a seguir, verifique e mostra qual a classificação dessa pessoa.

______________________________________________________________________
|Altura_________|_____________________Peso____________________________|
|               |Até 60  |  Entre 60 e 90 (Incluse)   |  Acima de 90  |
|Menor que 1,20 |    A   |              D             |       G       |
|De 1,20 a 1,70 |    B   |              E             |       H       |
|Maior que 1,70 |    C   |              F             |       I       |
______________________________________________________________________|
"""
while True:
    height = input("Digite a altura da pessoa : ")
    weight = input("Digite o peso da pessoa : ")
    try:
        height, weight = float(height), float(weight)
    except:
        print("Digito inválido")
    finally:
        if height < 1.20 and height > 0:
            if weight < 60:
                print("Categoria A")
            elif weight >= 60 and weight <= 90:
                print("Categoria D")
            elif weight > 90:
                print("Categoria G")
        elif height >= 1.20 and height <= 1.70:
            if weight < 60:
                print("Categoria B")
            elif weight >= 60 and weight <= 90:
                print("Categoria E")
            elif weight > 90:
                print("Categoria H")
        elif height > 1.70:
            if weight < 60:
                print("Categoria C")
            elif weight >= 60 and weight <= 90:
                print("Categoria F")
            elif weight > 90:
                print("Categoria I")
        else:
            print("Digito inválido.")

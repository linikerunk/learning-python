"""
Leia a distância em Km e a quantidade de listros de gasolina consumidos por um
carro em um percurso, calcule o consumo em Km/L e escreva uma mensagem de acordo
com a tabela abaixo.

    | CONSUMO    |   (Km/l)  |     MENSAGEM       |
    | menor que  |     8     |  Venda o carro!    |
    | entre      |   8 e 14  |     Econômico!     |
    | maior que  |     12    | Super econômico!   |
"""
while True:
    mileage = input ("Digite a distância em Km : ")
    liters = input("Digite quanto litros foi consumido no percurso : ")
    try:
        mileage, liters = float(mileage), float(liters)
    except:
        print("Digito inválido.")
    finally:
        consumption = mileage / liters
        if consumption > 12:
            print("Super Econômico!")
        elif consumption >= 8 and consumption <= 14:
            print("Econômico!") 
        else:
            print("Venda o carro!")
"""
Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de
acordo com a tabela abaixo:
______________________________________________________
|      IMC           |   Classificação               |
|--------------------|-------------------------------|
|  Menor que 18,5    |   Abaixo do Peso              |
| Entre 18,6 a 24,9  |     Saudável                  |
| Entre 25,0 a 29,9  |   Peso em Excesso             |
| Entre 30,0 a 34,9  |   Obsedidade Grau 1 (leve)    |
| Entre 35,0 a 39,9  |   Obsedidade Grau 2 (severa)  |
|  Acima de 40,0     |   Obsedidade Grau 3 (mórbida) |
|____________________|_______________________________|
"""

while True:
    height = input("Digite sua altura : ")
    weight = input("Digite seu peso : ")

    height = height.replace(",", ".")
    weight = weight.replace(",", ".")
    try:
        height, weight = float(height), float(weight)
    except:
        print("Digito inválido")
    finally:
        imc = (weight / height ** 2)
        if imc <= 18.5 and imc > 0:
            print(f"IMC : {round(imc, 2)} Abaixo do Peso.")
        elif imc > 18.5 and imc <= 24.9:
            print(f"IMC : {round(imc, 2)} Saudável.")
        elif imc >= 25 and imc <= 29.9:
            print(f"IMC : {round(imc, 2)} Peso em Excesso.")
        elif imc >= 30 and imc <= 34.9:
            print(f"IMC : {round(imc, 2)} Obsedidade Grau 1 (leve).")
        elif imc >= 35 and imc <= 40:
            print(f"IMC : {round(imc, 2)} Obsedidade Grau 2 (severa).")
        elif imc >40:
            print(f"IMC : {round(imc, 2)} Obsedidade Grau 3 (mórbida).")
        else:
            print("Cálculo inválido")
    cont = input("Deseja continuar : [SIM] ou [Qualquer outra coisa] : ")
    cont = cont.upper()
    if cont == "SIM":
        pass
    else:
        break
        
            

"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá
ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

________________________________________________________________________________________________
|  Venda mensal                                                      |         Comissão         |
|--------------------------------------------------------------------|--------------------------|
|Maior ou igual a R$ 100.000,00                                      |R$ 700,00 + 16% das vendas|
|Menor que R$ 100.000,00 e maior ou igual a R$ 80.000,00             |R$ 650,00 + 14% das vendas|
|Menor que R$ 80.000,00 e maior ou igual a R$ 60.000,00              |R$ 600,00 + 14% das vendas|
|Menor que R$ 60.000,00 e maior ou igual a R$ 40.000,00              |R$ 550,00 + 14% das vendas|
|Menor que R$ 40.000,00 e maior ou igual a R$ 20.000,00              |R$ 500,00 + 14% das vendas|
|Menor que R$ 20.000,00                                              |R$ 400,00 + 14% das vendas|
|____________________________________________________________________|__________________________|
"""

value = input("Digite o valor : ")
try:
    value = float(value)
except:
    print("Digito inválido.")
finally:
    if value > 100000:
        commission = (value * 0.16 + 700)
        print(f"Sua venda foi : {round(value, 2)}")
        print(f"Comissão do valor : R${round(commission, 2)}")

    elif value <= 100000 and value >= 80000:
        commission = (value * 0.14 + 650)
        print(f"Sua venda foi : {round(value, 2)}")
        print(f"Comissão do valor : R${round(commission, 2)}")

    elif value < 80000 and value >= 60000:
        commission = (value * 0.14 + 600)
        print(f"Sua venda foi : {round(value, 2)}")
        print(f"Comissão do valor : R${round(commission, 2)}")

    elif value < 60000 and value >= 40000:
        commission = (value * 0.14 + 550)
        print(f"Sua venda foi : {round(value, 2)}")
        print(f"Comissão do valor : R${round(commission, 2)}")

    elif value < 40000 and value >= 20000:
        commission = (value * 0.14 + 500)
        print(f"Sua venda foi : {round(value, 2)}")
        print(f"Comissão do valor : R${round(commission, 2)}")

    elif value < 20000:
        commission = (value * 0.14 + 400)
        print(f"Sua venda foi : {round(value, 2)}")
        print(f"Comissão do valor : R${round(commission, 2)}")

    else:
        print("Número negativo não é válido.")
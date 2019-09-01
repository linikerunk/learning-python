#Um posto de combustível vende três tipos de combustível: álcool, diesel
#e gasolina. O preço de cada litro de combustível é apresentado na tabela
#a seguir. Faça um programa que leia um caractere que representa
#o tipo de combustível comprado (a, d ou g) e a quantidade em litros.
#O programa deve imprimir o valor em reais a ser pago pelo combustível.

#A - Álcool ---1,7997
#D - Diesel ---0,9798
#G - Gasolina ---2,1009


tipo_combustivel = str(input(" \t Digite o tipo de combustível \n \t \
[A - Álcool], [D - Diesel], [G - Galosina] : "))
tipo_combustivel = tipo_combustivel.upper()
while len(tipo_combustivel) > len(tipo_combustivel[0]):
    if len(tipo_combustivel) > len(tipo_combustivel[0]):
        print('Valor inválido')
        tipo_combustivel = str(input(" \t Digite o tipo de combustível \n \t \
    [A - Álcool], [D - Diesel], [G - Galosina] : "))
    tipo_combustivel = tipo_combustivel.upper()

qnt_combustivel = float(input("Digite a quantidade que deseja colocar em Litros : "))
if tipo_combustivel == 'A':
    print(f'Você colocou {qnt_combustivel} no valor de [1,7997] \
total a pagar = R${qnt_combustivel * 1.7997:.3f}')
elif tipo_combustivel == 'D':
    print(f'Você colocou {qnt_combustivel} no valor de [0,9798] \
total a pagar = R${qnt_combustivel * 0.9798:.3f}')
elif tipo_combustivel == 'G':
    print(f'Você colocou {qnt_combustivel} no valor de [2,1009] \
total a pagar = R${qnt_combustivel * 2.1009:.3f}')



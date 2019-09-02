#Escreva um programa que pergunte o valor inicial de uma dívida e o juros mensal.
#Pergunte também o valor mensal que será pago. Imprima o número de meses para
#que a dívida seja paga, o total pago e o total de juros pago.

divida = float(input('Valor da divida : '))
taxa = float(input('Digite a taxa do juros mesal em % [sem o %] : '))
valor_pgt = float(input('Valor pago mensalmente : '))

meses_pgt = divida / valor_pgt
meses_pgt = int(meses_pgt)
print(f' Número de mêses para pagar a dívida : {meses_pgt} ')
print(f' Total  pago : {divida:.2f} \n')

cont = 0
for meses_pgt in enumerate(range(1, meses_pgt)):
    juros = divida * (taxa/100)
    divida = divida + juros - valor_pgt
    cont += juros
print(f' Total pago em juros : {cont:.2f}')

    
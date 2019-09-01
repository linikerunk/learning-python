#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
#elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para
#residências, I para indústrias e C para comércios. Calcule o preço a pagar,
#de acordo com a tabela a seguir.

qtd_energia = float(input(' Quantidade de Kwh Consumida : '))
instalacao = str(input(' Tipo de instalação :\n \
R -> residências :\n \
I -> Indústrias :\n \
C -> Comércios :\n'))

instalacao =instalacao[0].upper()

if instalacao == 'R':
    if qtd_energia <= 500:
        print(f' Faixa Residencial (kwh <= 500 R$ 0,40) Total a se pagar: {qtd_energia * 0.40}')
    elif qtd_energia > 500:
        print(f' Faixa Residencial (kwh > 500 R$ 0,65) Total a se pagar: {qtd_energia * 0.65}')

if instalacao == 'C':
    if qtd_energia <= 1000:
        print(f' Faixa Comercial (kwh <= 1000 R$ 0,55) Total a se pagar: {qtd_energia * 0.55}')
    elif qtd_energia > 1000:
        print(f' Faixa Comercial (kwh > 1000 R$ 0,60) Total a se pagar: {qtd_energia * 0.60}')

if instalacao == 'I':
    if qtd_energia <= 5000:
        print(f' Faixa Industrial (kwh <= 5000 R$ 0,55) Total a se pagar: {qtd_energia * 0.55}')
    elif qtd_energia > 5000:
        print(f' Faixa Industrial (kwh > 500 R$ 0,60) Total a se pagar: {qtd_energia * 0.60}')

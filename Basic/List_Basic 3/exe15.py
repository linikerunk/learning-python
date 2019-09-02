#Escreva um programa para controlar uma pequena máquina registradora.
#Você deve solicitar ao usuário que digite o código do produto e a quantidade
#comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto.
#Código	Preço
#1	0,50
#2	1,00
#3	4,00
#5	7,00
#9	8,00
#Seu programa deve exibir o total de compras depois que o usuário digitar 0.
#Qualquer outro código deve gerar a mensagem de erro "Código inválido".

valor_codigo = 0
cont = 0
codigo = ""
while codigo != 0:
    print('TABELA DE CÓDIGOS \n\
    Código	Preço\n\
    1  -    0.50\n\
    2  -    1.00\n\
    3  -    4.00\n\
    5  -    7.00\n\
    9  -    8.00\n\
    ')
    codigo = int(input('Digite o código do Produto : '))
    if codigo == 0:
        print(f'Total de items comprados {cont}')
        print(f'Valor das compras foram : {valor_codigo}')
        exit(1)
    qnt_codigo = int(input('Quantidade Comprada : '))
    if codigo == 1:
        valor = qnt_codigo * 0.5
        valor_codigo += valor
        cont += qnt_codigo
    elif codigo == 2:
        valor = qnt_codigo * 1.0
        valor_codigo += valor
        cont += qnt_codigo
    elif codigo == 3:
        valor = qnt_codigo * 4.0
        valor_codigo += valor
        cont += qnt_codigo
    elif codigo == 5:
        valor = qnt_codigo * 7.0
        valor_codigo += valor
        cont += qnt_codigo
    elif codigo == 9:
        valor = qnt_codigo * 8.0
        valor_codigo += valor
        cont += qnt_codigo
    else :
        print('Código Inválido')




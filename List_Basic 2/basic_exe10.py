#Imagine uma prova com 100 questões, em que cada uma delas vale 1 ponto.
#Nesse caso, faça um programa para divulgar o
#resultado a partir de conceitos, de acordo com a seguinte tabela:
#Pontos	Conceito
#Menor ou igual a 50	D
#Maior que 50 e menor ou igual a 70	C
#Maior que 70 e menor ou igual a 90	B
#Maior que 90 e menor ou igual a 100	A

################################################################################

while True:
    result_test = input('Digite quantas questões você acertou (Digite [sair] para sair.) : ')
    result_test = result_test.upper()

    if str(result_test) == 'SAIR':
        print('Desligando Sistema...')
        exit(1)

    if int(result_test) <= 50 and int(result_test) >= 0:
        print(" Voce tirou [D]")

    if int(result_test) > 50 and int(result_test) <= 70:
        print(" Voce tirou [C]")

    if int(result_test) > 70 and int(result_test) <= 90:
        print(" Voce tirou [B]")

    if int(result_test) > 90 and int(result_test) <= 100:
        print(" Voce tirou [A]")

    elif int(result_test) < 0 or int(result_test) > 100:
        print('Valor Inválido...')
    

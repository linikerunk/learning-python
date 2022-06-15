#Elabore um programa, que solicite ao usuário a velocidade do veículo e
#apresente na tela a penalidade, de acordo com a tabela a seguir:

#Velocidade	Penalidade
#Menor ou igual a 60	Sem Penalidade
#Maior que 60 e menor ou igual a 80	Multa Leve
#Maior que 80 e menor ou igual a 100	Multa Grave
#Maior que 100 e menor ou igual a 120	Multa Gravíssima
#Maior que 120	Detenção do Condutor

################################################################################
while True:
    tela = "***"
    print(tela * 15+" MENU"+tela * 25)
    velocidade = input("Digite a velocidade quem você estava em KM/H \
    \n caso prefira em M/S digite: 'MS' [* DIGITE EXIT PARA SAIR *]:")
    velocidade = velocidade.upper()

    if velocidade == 'EXIT':
        print('Desligando Sistema...')
        exit(1)

    elif velocidade != 'MS' and float(velocidade) >0:
        velocidade = float(velocidade)
        if velocidade <= 60: print('Você não teve penalidade..')
        elif velocidade > 60 and velocidade <= 80: print('Você recebeu uma Multa Leve..')
        elif velocidade > 80 and velocidade <= 100: print('Você recebeu uma Multa Grave..')
        elif velocidade > 100 and velocidade <= 120: print('Você recebeu uma Multa Gravíssima...')
        else: print('Você está detido.. (Detenção do Condutor)')

    elif velocidade == 'MS':
        velocidade = float(input("Digite a velocidade em MS:"))
        if velocidade < 0:
            print('Não Existe velocidade negativa (Desprezando a regra da macha Ré) ')
            velocidade = input("Digite a velocidade em M/S:")
        else:
            velocidade = velocidade * 3.6
            if velocidade <= 60: print('Você não teve penalidade..')
            elif velocidade > 60 and velocidade <= 80: print('Você recebeu uma Multa Leve..')
            elif velocidade > 80 and velocidade <= 100: print('Você recebeu uma Multa Grave..')
            elif velocidade > 100 and velocidade <= 120: print('Você recebeu uma Multa Gravíssima...')
            else: print('Você está detido.. (Detenção do Condutor)')

    elif float(velocidade) < 0:
        print('Não Existe velocidade negativa (Desprezando a regra da macha Ré) ')
        velocidade = input("Digite a velocidade em KM/H caso prefira em M/S digite [MS] :")
    elif int(velocidade) == 0:
        print(' Você não acelerou ainda...')



#Escreva um programa que pergunte o depósito inicial, a taxa de juros
#de uma poupança e o valor depositado mensalmente. Esse valor será depositado
#no início de cada mês e você deverá considerá-lo para o cálculo de juros do mês
#seguinte. Exiba os valores mês a mês para os 24 primeiros meses.
#Escreva o total ganho com juros no período.

sistem = 0
while sistem != 'NAO':
    sistem = str(input("Deseja fazer uma consulta -- digite [SIM] ou [NAO] : "))
    sistem = sistem.upper()
    if sistem == 'SIM':
        deposito = float(input('Digite o valor do Depósito : '))
        taxa = float(input('Digite a taxa de Juros em % [sem o %] : '))
        cont = 25
        valor_juros_total = 0
        for mes, cont in enumerate(range(1, cont)):
            juros = deposito * (taxa/100)
            print(f"Juros Taxa mês {mes+1} : ", round(juros, 2) )
            deposito = deposito + juros
            print(f"Valor Total mês {mes+1} : ", round(deposito, 2))
            print("\n")
            valor_juros_total += juros
            cont -= 1
            mes += 1
        print(f'Com o valor do deposito de : {deposito:.2f}, você teve uma retenção de juros\n\
        total de {valor_juros_total:.2f}')
    elif sistem == 'NAO':
        print('Até mais...')
        exit(1)
    elif sistem != 'SIM' and sistem != 'NAO':
        print('Informação digitada inválida..')
        exit(1)
#Escreva um programa que pergunte o depósito inicial e a taxa de juros
#de uma poupança. Exiba os valores mês a mês para
#os 24 primeiros meses. Escreva o total ganho com juros no período.

deposito = float(input('Digite o valor do Depósito : '))
taxa = float(input('Digite a taxa de Juros % [sem o %] : '))

cont = 25
for mes, cont in enumerate(range(1, cont)):
    juros = deposito * (taxa/100)
    print(f"Juros Taxa mes {mes+1} : ", round(juros, 2) )
    deposito = deposito + juros
    print(f"Valor Total mes {mes+1} : ", round(deposito, 2))
    print("\n")
    cont -= 1
    mes += 1
    
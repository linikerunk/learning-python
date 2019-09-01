#1) Escreva um programa que pergunte a velocidade
#do carro de um usuário. Caso ultrapasse 80 km/h,
#exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = float(input('Digite a velocidade do carro  Km/h: '))

if velocidade > 80:
    print('Você  foi multado..')
    total = (velocidade - 80) * 5
    print(f'Valor da Multa {total} R$')
else:
    print('Você está no limite de velocidade.')

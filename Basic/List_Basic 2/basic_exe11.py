#Tendo como dados de entrada a altura e o sexo de uma pessoa, faça um programa 
#que calcule seu peso ideal, utilizando as seguintes fórmulas:
#- para homens: (72.7 * h) - 58;
#- para mulheres: (62.1 * h) - 44.7.

while True:
    sistem = str(input('Ir para o iniciar o sistema digite [iniciar] para desligar digite \
[desligar] : '))
    sistem = sistem.upper()
    if sistem == 'INICIAR':
        sexo = str(input('Digite seu sexo : [F] Feminino, [M] Masculino: '))
        sexo = sexo.upper()
        altura = float(input('Digite seu Altura : '))
        print(altura)
        if sexo == 'F':
            imc = (62.1 * altura)-44.7
            print(f' Seu Peso ideial é : : {imc:.2f}')
        elif sexo == 'M':
            imc = (72.7 * altura)-58
            print(f' Seu Peso ideial é : {imc:.2f}')
    elif sistem == 'DESLIGAR':
        print('Saindo do Sistema..')
        exit(1)
    else : 
        print('Digito invalido...')

    


    
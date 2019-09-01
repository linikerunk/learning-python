#Faça um programa para ler três números e informar se eles
#podem ou não ser lados de um triângulo. Caso os lados formem
#um triângulo, indique se o mesmo é: equilátero, isósceles ou escaleno.
#Observação: Um triângulo é equilátero quando possui os três lados iguais,
#isósceles quando possui dois lados iguais e escaleno quando não possui
#nenhum dos lados iguais.
while True:
    sistem = str(input('iniciar - Iniciar Sistema \ndesligar - Desligar Sistema: '))
    sistem = sistem.upper()

    if sistem == 'DESLIGAR':
        print('Desligando Sistema...')
        exit(1)

    elif sistem == 'INICIAR':
        angulo1 = float(input('Digite o Primeiro valor : ')) 
        angulo2 = float(input('Digite o Segundo valor : '))
        angulo3 = float(input('Digite o Terceiro valor : '))

        soma_angulos = angulo1 + angulo2 + angulo3

        if soma_angulos != 180 or soma_angulos <= 0:
            print('Os valores fornecidos não se encaixam dentro do parâmetro de um triangulo.')
        
        else:
            if angulo1 == angulo2 and angulo1 == angulo3:
                print('Os valores fornecido forma um triângulo equilátero..')
            elif angulo1 == angulo2 or angulo2 == angulo3 or angulo1 == angulo3:
                print('Os valores fornceidos formam um triângulo isósceles...')
            else:
                print('Os valores fornecidos formam um triângulo escaleno..')
    else: 
        print('Valor Invalido..')
        


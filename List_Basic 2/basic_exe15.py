#Faça um programa para calcular o peso ideal,
#a partir da fórmula IMC = peso / altura2. Nesse caso,
#solicite o peso e a altura do usuário, faça o cálculo e apresente
#a faixa de risco correspondente, de acordo com a tabela seguinte:
#*************************************
#IMC	Faixa de Risco
#Abaixo de 20	Abaixo do peso
#A partir de 20 até 25	Normal
#Acima de 25 até 30	Excesso de peso
#Acima de 30 até 35	Obesidade
#Acima de 35	Obesidade mórbida
#*************************************

peso = float(input('Digite seu Peso : '))
altura = float(input('Digite sua Altura : '))
imc = (peso / altura ** 2)


if imc < 20 and imc > 0:
    print('Você está a baixo do peso.')

elif imc >= 20 and imc < 25:
    print('Você está no peso.')

elif imc > 25 and imc < 30:
    print('Voçe está com Excesso de peso.')

elif imc > 30 and imc < 35:
    print('Obesidade')

elif imc > 35:
    print('Obesidade Mórbida')

    



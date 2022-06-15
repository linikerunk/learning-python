#Faça um programa para imprimir a tabuada, de forma que o usuário digite o início
#e o fim da tabuada, em vez de começar com 1 e 10.

ini_tabuada = int(input('Digite onde a tabuada irá começar : '))
fim_tabuada = int(input('Digite onde a tabuada irá acabar : '))


for elem in range(ini_tabuada, fim_tabuada+1):
    print(f'{elem} x {ini_tabuada} = {elem * ini_tabuada }')
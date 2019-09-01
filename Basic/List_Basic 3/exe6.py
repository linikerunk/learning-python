#Faça um programa para imprimir a tabuada de um número
#digitado pelo usuário. Nesse caso, imprimir os resultados no mesmo formato
#de uma tabuada: 2 x 1 = 2, 2 x 2 = 4, ... 

tabuada = int(input(' Digite o número que deseja saber a tabuada: '))

for elem in range(0, 11):
    print(f'{elem} x {tabuada} = {elem * tabuada}')
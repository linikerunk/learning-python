#Faça um programa para imprimir de 1 até o número digitado pelo usuário, mas,
#dessa vez, apenas os números ímpares.

numero = int(input('Digite o número desejado de iterações : '))

for item in range(1, numero):
    if item % 2 != 0:
        print(item)
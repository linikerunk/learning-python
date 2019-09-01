#Faça um programa que receba três notas e seus respectivos pesos,
#calcule e mostre a média ponderada desses valores.

notas = []; pesos = []; soma_pond = 0; media_pond = 0; soma_peso = 0

for nota, peso in enumerate(range(3)):
    notas = input(f'Digite a {nota + 1} nota: ')
    peso = input(f'Digite o peso da nota{nota + 1}: ')
    soma_peso += int(peso)
    print(soma_peso)
    soma_pond += int(notas) * int(peso)
media_pond = soma_pond / soma_peso

print(f'A média ponderada das 3 notas : {media_pond:.2f}')
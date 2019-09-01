#Faça um programa que receba três notas,
#calcule e mostre a média aritmética entre elas.

notas = []
soma = 0
for notas in range(3):
    notas = input(f'Digite a {notas+1} nota : ')
    soma += int(notas)

media = (soma / 3 )
print(f'A Média Aritmética das 3 notas foi: {media:.2f}')

# Escreva um programa que pergunte a quantidade de km percorrido por um carro
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia
# e R$ 0,15 por km rodado.

km_percorrido = float(input("Quantidade de KM percorrido pelo carro : "))
qnt_dias = int(input("Quantidade de dias que o carro foi alugado : "))

preco_a_pagar = ((qnt_dias * 60) + (km_percorrido * 0.15))
print(f'O Preço a pagar pela quantidade de dias : {qnt_dias}\n \
e a quilometragem percorrida : {km_percorrido} \n \
é igual a : {preco_a_pagar} valor.')

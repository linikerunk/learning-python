#Faça um programa que solicite o preço de uma mercadoria e o percentual
#de desconto. Exiba o valor do desconto e o preço a pagar.

preco = float(input("Digite o preço da mercadoria : "))
per_desconto = float(input("Digite o percentual de desconto "))

valor_desc = float(preco * (per_desconto/100))

print(f'O valor do desconto foi : {valor_desc:.2f}')
print(f'O preço com desconto a pagar : {preco - valor_desc:.2f}')

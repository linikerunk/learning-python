"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, 
tendo em vista que o desconto foi de 12%
"""

while True:
    try:
        valor = float(input("Digite o valor do produto : "))
        novo_valor =  valor + (valor * 0.12)
        print(f"valor com 12% de desconto : {round(novo_valor, 2)}")
    except:
        print("Digito Inválido.")
"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa
diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%;). Faça um programa em que 
o usuário entre com o valor eo estado destino do produto e o programa retorne o preço final do produto
acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar
uma mensagem de erro.
"""

while True:
    estate = input("Digite o a sigla do estado: [SP - São Paulo, RJ - Rio de Janeiro, etc...] : ")
    product = input("Digite o valor do produto antes do calculo do ICMS : ")

    try:
        estate, product = str(estate).upper(), float(product)
    except:
        print("Digito inválido, digite novamente.")
    finally:
        if estate == "SP":
            product_final = (product * 0.12) + product
            print(f"Preço final do produto com imposto do estado onde foi negociado e {product_final}")
        elif estate == "MG":
            product_final = (product * 0.07) + product
            print(f"Preço final do produto com imposto do estado onde foi negociado e {product_final}")
        elif estate == "RJ":
            product_final = (product * 0.15) + product
            print(f"Preço final do produto com imposto do estado onde foi negociado e {product_final}")
        elif estate == "MS":
            product_final = (product * 0.08) + product
            print(f"Preço final do produto com imposto do estado onde foi negociado e {product_final}")
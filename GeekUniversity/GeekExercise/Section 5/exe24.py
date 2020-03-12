"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa
diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%;). Faça um programa em que 
o usuário entre com o valor eo estado destino do produto e o programa retorne o preço final do produto
acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar
uma mensagem de erro.
"""

estate = input("Digite o a sigla do estado: [SP - São Paulo, RJ - Rio de Janeiro, etc...] : ")
product = input("Digite o valor do produto antes do calculo do ICMS : ")

try:
    estate, product = str(estate).upper(), float(product)
except:
    print("Digito inválido, digite novamente.")
finally:
    if estate == "SP":
        print("São Paulo")
    elif estate == "MG":
        pass
    elif estate == "RJ":
        pass
    elif estate == "MS":
        pass
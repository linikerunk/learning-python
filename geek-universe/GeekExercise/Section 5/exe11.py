"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na 
tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 correspon-
derá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o pro-
grama terminará com a mensagem "Número Inválido"
"""

number = input("Digite um número : ")
try:
    number = float(number)
except:
    print("Digito inválido.")
finally:
    if number < 0:
        print("Número inválido.")
    else:
        number = str(number).replace(".", "")
        soma = 0
        for alg in (number[:-1]):
            soma = soma + float(alg)
        print(f" A soma de todos os seus algarismos é {soma}")
            
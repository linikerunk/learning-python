"""
Escreava um algoritmo que leia um número inteiro entre 100 e 999 e imprima na
saída cada um dos algarismos que compõem o número.
"""

digit = input("Digite um número inteiro entre 100 e 999 : ")
try:
    digit = int(digit)
except:
    print("Digito inválido.")
finally:
    if digit < 100 or digit > 999:
        print("Digito inválido.")
    else:
        for dig in str(digit):
            print(dig, "\t")
"""
https://a2.udemycdn.com/2019-02-11_23-39-39-f2d5ad686cf6c8986ae0313b46706118/original.pdf?nva=20200306083247&token=0c6d49bafc0535a119d31
"""

""" 
Faça um programa que leia um número inteiro e o imprima

"""
while True:
    numero = input("Digite um número:")
    try:
        numero = int(numero)
        break
    except:
        print("numero não é um digito..")

print(f"Número digitado : {numero}")

"""
Faça um programa que mostre ao usuário um menu com 4 opçoes de operações matematicas ( as bássicas, por exemplo). O usuário escolhe
uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo. 
"""

while True:
    print(""" ***************** MENU ******************* \n
    [1] - [    Somar    ]\t \n
    [2] - [   Subtrair  ]\t \n
    [3] - [ Multiplicar ]\t \n
    [4] - [   Divisão   ]\t \n
*******************************************
    """)
    options = input("Digite uma opção válida de 1 a 4 : ")
    try:
        options = float(options)
    except:
        print("O valor deve ser um número.")
    finally:
        pass
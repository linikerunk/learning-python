"""
Faça um programa que mostre ao usuário um menu com 4 opçoes de operações matematicas ( as bássicas, por exemplo). O usuário escolhe
uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo. 
"""

while True:
    def somar(number_1, number_2):
        soma = number_1 + number_2
        print(f"\n A soma dos números é : {round(soma, 2)}")
    
    def subtrair(number_1, number_2):
        subtracao = number_1 - number_2
        print(f"\n A subtração dos números é : {round(subtracao, 2)}")
    
    def multiplicar(number_1, number_2):
        multiplicacao = number_1 * number_2
        print(f"\n A multiplicação dos números é : {round(multiplicacao, 2)}")

    def dividir(number_1, number_2):
        try:
            divisao = number_1 / number_2
            print(f"\n A divisão dos números é : {round(divisao, 2)}")
        except:
            print("Dividir por Zero não é permitido")
        finally:
            pass


    print(""" ***************** MENU ******************* \n
    [1] - [    Somar    ]\t \n
    [2] - [   Subtrair  ]\t \n
    [3] - [ Multiplicar ]\t \n
    [4] - [   Dividir   ]\t \n
*******************************************
    """)
    options = input("Digite uma opção válida de 1 a 4 : ")
    try:
        options = float(options)
    except:
        print("O valor deve ser um número.")
    finally:
        if options < 1 or options > 4:
            print("DIGITO INVÁLIDO, DEVE ESTAR ENTRE 1 E 4. \n \n")
        else:
            number_1 = input("\nDigite o primeiro número : ")
            number_2 = input("\nDigite o segundo número : ")
            try:
                number_1, number_2 = float(number_1), float(number_2)
            except:
                print("Digito inválido.")    
            finally:
                options = {
                    1: somar(number_1, number_2),
                    2: subtrair(number_1, number_2),
                    3: multiplicar(number_1, number_2),
                    4: dividir(number_1, number_2),
                }
                

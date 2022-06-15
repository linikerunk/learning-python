"""
Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou 5,
mas não simultaneamente pelo dois.
"""

while True:
    number = input("Digite um número para verificar se é divisível por 3 ou 5 : ")
    try:
        number = float(number)
    except:
        print("Digito inválido.")
    finally:
        if number % 3 == 0 and number % 5 == 0:
            print("Esse número é divisível por 3 e 5 ao mesmo tempo ")
        elif number % 3 == 0:
            print("Número divisível por 3.")
        elif number % 5 == 0:
            print("Número divisível por 5.")
        else:
            print("Número não é divisivel por 3 ou por 5")
"""
Calcule as raízes da equação de 2º grau
    Lembrando que : x = -b +/- raiz(delta)/ (2.a)
    Delta = b² - 4.a.c
    Expressao = ax² + bx + c = 0
    A variavel a tem que ser diferente de zero. Caso seja igual, imprima mensagem
    "Não é equação de segundo grau".

    * Se Delta < 0, não existe real. Imprima a mensagem Não existe raiz.
    * Se Delta = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única
    * se Delta >= 0, imprima as duas raízes são reais 
"""

import math

while True:
    print("Digite a expressa ax^2 + bx + c = 0. \n")
    a = input("Digite o valor de a : ")
    b = input("Digite o valor de b : ")
    c = input("Digite o valor de c : ")
    try:
        a, b, c = float(a), float(b), float(c)
    except:
        print("Digito inválido.")
    finally:
        delta = ((b**2) - 4 * a * c) 
        if delta < 0:
            print("Não existe raiz.")
            exit()
        elif delta == 0:
            print("Raiz única.")
        elif delta > 0:
            print("as duas raízes são reais")

        x1 = ((-b) + math.sqrt(delta))/ (2 * a)
        x2 = ((-b) - math.sqrt(delta))/ (2 * a)

        print(f"A equação {a}X^2 + {b}X + {c} = 0, tem seu X1 : {x1} ")
        print(f"A equação {a}X^2 + {b}X + {c} = 0, tem seu X2 : {x2} \n\n")
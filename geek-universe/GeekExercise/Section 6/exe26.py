"""
Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um núme-
ro dado.
"""


def dividers(num):
    for num in range(1, int(num)+1):
        if num % 11 == 0 and num == 11:
            print("divisivel por 11 : ", num)
            yield num
        elif num % 13 == 0 and num == 13:
            print("divisivel por 13 : ", num)
            yield num
        elif num % 17 == 0 and num == 17:
            print("divisivel por 17 : ",num)
            yield num
        

number = input("Digite um número maior que 17 : ")
try:
    number = float(number)
except:
    print("Digito inválido")
finally:
    if number < 17:
        print("Digito inválido.")
    else:
        print(list(dividers(number)))

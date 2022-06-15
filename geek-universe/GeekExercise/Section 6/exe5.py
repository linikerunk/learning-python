"""
Faça um program que peça ao usuário para digitar 10 valores e some-os
"""

cont = 0
sum_of_number = 0

while cont < 10:
    number = input("Digite um número : ")
    try:
        number = float(number)
    except:
        print("Digito inválido.")
    sum_of_number  +=  number
    cont += 1

print(f"A soma de todos os números é igual a : {round(sum_of_number, 2)}") 
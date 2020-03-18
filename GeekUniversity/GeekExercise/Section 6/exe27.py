"""
Em matemática, o número harmônico designado por H(n) define-se como sendo a soma
da série harmônica:
            H(n) = 1 + 1/2 + 1/3 + 1/4 ... + 1/n
"""

def average_harmonica(numbers, quantity):
    sum_of_numbers_reversed = 0
    print("tamanho dos numbers :", numbers)
    for denominer in range(len(numbers) + 1):
        if denominer == 0:
            pass
        else:
            sum_of_numbers_reversed  += (1 / denominer)
    average_harmonica = quantity / sum_of_numbers_reversed
    print("Média Harmônica : ", average_harmonica)

quantity = input("Total de números que deseja verificar : ")
try:
    quantity = int(quantity)
except:
    print("Digito inválido.")
numbers = []

for number in range(0, quantity):
    number = input("Digite um Número : ")
    try:
        number = float(number)
    except:
        print("Digito inválido.")
    finally:
        numbers.append(number)

average_harmonica(numbers, quantity)
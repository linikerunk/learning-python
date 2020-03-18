"""
Escreva um programa para calcular o valor de série, para 5 termos
"""

def factorial(number):
    result=1
    counter=1
    while counter <= number:
        result *= counter
        counter += 1
    return result


expression = 0
numbers = []

for number in range(1, 6):
    number = input("Digite um número para calcularmos:")
    try:
        number = float(number)
    except:
        print("Digito inválido")
    finally:
        numbers.append(number)

expression = (expression + (1 / factorial(numbers[0])) + (1 / factorial(numbers[1])) + \
(1 / factorial(numbers[2])) + (1 / factorial(numbers[3])) + (1 / factorial(numbers[4]))) 

print("Soma da expressão : ", expression)


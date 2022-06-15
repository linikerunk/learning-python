"""
Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor
E, conforme a fórmula a seguir.
            E = 1 + 1/1! + 1/2! + 1/3! + 1/N!
"""

def factorial(number):
    result=1
    counter=1
    while counter <= number:
        result *= counter
        counter += 1
    return result

number = input("Digite um número para calcularmos:")
try:
    number = float(number)
except:
    print("Digito inválido.")

expression =  1
for num in range(1, int(number) + 1):
    # print("fatorial :", factorial(num))
    expression = expression + (1/ factorial(num)) 
print("Soma dos fatoriais : ", expression)




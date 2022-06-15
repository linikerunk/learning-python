"""
Faça um programa que receba dois números. Calcule e mostre:
    * A soma dos números pares desse intervalo de números, incluindo os números
    digitados;
    * a multiplicação dos números ímpares desse intervalo, incluindo os digita
    dos;
"""

number_one = input("Digite o primeiro número : ")
number_two = input("Digite o segundo número : ")
try:
    number_one, number_two = int(number_one), int(number_two)
except:
    print("Digito inválido.")
finally:
    sum_of_range = 0; mul_of_range = 1
    if number_two > number_one:
        for num in range(number_one, number_two+1, 1):
            if num % 2 == 0:
                sum_of_range += num
            else:
                mul_of_range = num * mul_of_range
        print(f"SOMA : {sum_of_range}")
        print(f"MULTIPLICAÇÂO: {mul_of_range}")
    else:
        for num in range(number_two, number_one+1, 1):
            if num % 2 == 0:
                sum_of_range += num
            else:
                mul_of_range = num * mul_of_range
        print(f"SOMA : {sum_of_range}")
        print(f"MULTIPLICAÇÂO: {mul_of_range}")
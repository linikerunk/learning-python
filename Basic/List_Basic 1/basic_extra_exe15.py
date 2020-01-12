'''

Devido à proximidade com o Dia do Trabalho, uma empresa resolveu conceder aumentos salariais a seus funcionários.
Aqueles com salário superior a R$ 500, terão aumento de 10%, enquanto os que ganham mais de R$ 300 terão aumento de 7%.
Os demais funcionários terão aumento de apenas 5%. Escreva um programa que receba como entrada o salário atual de um funcionário,
calcule e exiba o valor de seu novo salário já com o aumento concedido.

'''

import math
import re


__author__ = 'Liniker'


def main():
    salario = float(input())

    if salario > 500:
        novo_salario = salario * 0.10
        salario = salario + novo_salario
        print(f'{salario:.2f}')
    elif salario > 300 and salario < 500:
        novo_salario = salario * 0.07
        salario = salario + novo_salario
        print(f'{salario:.2f}')
    else:
        novo_salario = salario * 0.05
        salario = salario + novo_salario
        print(f'{salario:.2f}')


if __name__ == "__main__":
    main()

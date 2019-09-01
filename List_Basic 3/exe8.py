# Escreva um programa que leia dois números.
# Imprima o resultado da multiplicação do primeiro pelo segundo.
# Utilize apenas os operadores de soma e subtração para calcular o resultado.
# Lembre-se de que podemos entender a multiplicação de dois números como somas
# sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

def multiplica(numero1, numero2):
    resultado = 0
    for i in range(0, int(numero2)):
        resultado = numero1 + resultado
    return resultado

def main():
    numero1 = float(input('Digite o Primeiro número : '))
    numero2 = float(input('Digite o Segundo número : '))
    print(multiplica(numero1, numero2))


if __name__ == '__main__':
    main()
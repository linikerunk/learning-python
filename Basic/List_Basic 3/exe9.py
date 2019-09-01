#Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro
#pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de
#soma e subtração para calcular o resultado. Lembre-se de que podemos entender
#o quociente da divisão de dois números como a quantidade de vezes que podemos
#retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair
#4 cinco vezes de 20.


def divisao(numero1, numero2):
    resultado = 0
    for i in range(0, int(numero2)):
        resultado = numero1 
    return resultado

def main():   
    numero1 = float(input('Digite o primeiro Número : '))
    numero2 = float(input('Digite o segundo Número : '))
    print(divisao(numero1, numero2))

if __name__ == '__main__':
    main()
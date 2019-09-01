#Escreva um programa que leia dois números e que pergunte qual operação você
#deseja realizar: soma (+), subtração (-), multiplicação (*) e divisão (/).
#Exiba o resultado da operação solicitada.

def operacao(numero_1, numero_2):
    print(f' Qual operação você deseja realizar (exemplo: Soma) : ')
    operacao = str(input('Soma (+):\n  \v \
Subtração (-):\n  \v\
Multiplicação (*):\n  \v\
Divisão (/):\n \v'))
    
    resultado(operacao, numero_1, numero_2)

def resultado(operacao, numero_1, numero_2):
    if operacao == 'Soma':
        print(f'Soma do  1 número: {numero_1} e do 2 número : {numero_2} \n')
        print(f'Resultado : {numero_1 + numero_2}')
    if operacao == 'Subtração':
        print(f'Subtração do  1 número: {numero_1} e do 2 número : {numero_2} \n')
        print(f'Resultado : {numero_1 - numero_2}')
    if operacao == 'Multiplicação':
        print(f'Multiplicação do  1 número: {numero_1} e do 2 número : {numero_2} \n')
        print(f'Resultado : {numero_1 * numero_2}')
    if operacao == 'Divisão':
        print(f'Divisão do  1 número: {numero_1} e do 2 número : {numero_2} \n')
        print(f'Resultado : {numero_1 / numero_2}')


def main():
    numero_1 = float(input(' Digite um número : '))
    numero_2 = float(input(' Digite um outro número : '))
    operacao(numero_1, numero_2)


if __name__ == "__main__":
    main()
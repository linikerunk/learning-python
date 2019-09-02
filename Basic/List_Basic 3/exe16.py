#Escreva um programa que exiba uma lista de opções (menu): adição, subtração,
#divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
#Repita até que a opção saída seja escolhida.

def menu():
    menu = False
    while menu != True:
        print('**'*20 +'MENU'+ '**'*20)
        menu = str(input('Digite a opção desejada: \n\
    *-[ADICAO]\n\
    *-[SUBTRACAO]\n\
    *-[DIVISAO]\n\
    *-[MULTIPLICACAO]\n\
    *-[SAIR] : '))
        menu = menu.upper()
        if menu == 'ADICAO':
            numero = float(input('Digite um número para fazer a opção de ADIÇÃO: '))
            tabuada = int(input('Digite a quantidade de iteração com esse número : '))
            adicao(x=numero, y=tabuada)

        elif menu == 'SUBTRACAO':
            numero = float(input('Digite um número para fazer a opção de SUBTRAÇÃO: '))
            tabuada = int(input('Digite a quantidade de iteração com esse número : '))
            subtracao(x=numero, y=tabuada)

        elif menu == 'DIVISAO':
            numero = float(input('Digite um número para fazer a opção de DIVISÃO: '))
            tabuada = int(input('Digite a quantidade de iteração com esse número : '))
            divisao(x=numero, y=tabuada)

        elif menu == 'MULTIPLICACAO':
            numero = float(input('Digite um número para fazer a opção de MULTIPLICAÇÃO: '))
            tabuada = int(input('Digite a quantidade de iteração com esse número : '))
            multiplicacao(x=numero, y=tabuada)

        elif menu == 'SAIR':
            sair()
        else:
            print('Dígito Inválido....')

def adicao(x, y):
    for i in range(y+1):
        print(f'{x:.1f} + {i:.1f} = {x+i:.1f}')

def subtracao(x, y):
    for i in range(y+1):
        print(f'{x:.1f} - {i:.1f} = {x-i:.1f}')

def multiplicacao(x, y):
    for i in range(y+1):
        print(f'{x:.1f} * {i:.1f} = {x*i:.1f}')

def divisao(x, y):
    for i in range(1 ,y+1):
        print(f'{x:.1f} / {i:.1f} = {x/i:.1f}')


def sair():
    print('Fechando Sistema, até mais...')
    exit(1)

if __name__ == '__main__':
    menu()
"""
Funções com retorno


OBS : Em Python, quando uma função nao retorna nenhum valor ele sempre volta None
"""

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()

print(f'Retorno {ret}')

# Vamos refatorar essa função para que ela retorno o valor

def quadrado_de_7():
    return (7 * 7) 

# Criamos uma variável para receber o retorno de uma função..
ret = quadrado_de_7()

print(f'Retorno {ret}')

# Refatorando a primeira função

def diz_oi():
    return "Oi"

print(diz_oi())

alguem = 'Pedro!'

print(diz_oi() +" "+ alguem)

"""
OBS: 1 - return ela finaliza a função;
     2 - podemos ter em uma funação diferentes returns;
     3 - podemos em uma função retornar qualquer tipo de dados e até mesmo multiplos valores
"""

# Exemplo 1

def diz_oi():
    print("Estou sendo executado antes o retorno...")
    return 'Oi';
    print("Estou sendo executado após o retorno...") # Não será executada

print(diz_oi())


# Exemplo 2

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao() # Desempacotando ..
print(num1, num2, num3, num4)


# Vamos criar uma função par jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

#Erros na utilização do retorno, que na verdade nem é erro, mas sim codificação
# desnecessária

def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())
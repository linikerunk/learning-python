"""
Funções de maior Grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação permite nos usarmos esse conceito HOF
indica que podemos ter funções que retornam outras funções como resultado ou mesmo
que podemos passar funçoes como argumentos para outras funções, e ate mesmo criar
variáveis do tipo de funções nos nossos programas.

OBS : Na seção de funçõesm nos utilizamos isso.

Em Python, as funções são Cidadãos de Primeira Classe, First Class Citizen
"""

# Exemplo - Definindo as funções


def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções:

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))


# Nested Functions - Funções Aninhadas

"""
Em Python podemos também ter funçoes dentro de funções, que são conhecidas como
Nested Functions ou também Inner Functions Internas
"""

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ae? ', "Suma daqui ", "Gosto Muito de você "))
    return humor() + pessoa

# Testando

print(cumprimento("Angelina"))
print(cumprimento("Claudiana"))



# Retornando Funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahaha', 'kkkkkkkkkkk', 'uhueahuehaeueuah'))
    return rir

rindo = faz_me_rir()
print(rindo())


# Inner Functions ( Funções Internas / Nested Functions ) podem acessar o escopo
# de funções mais externas.


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'lolololololol', 'kkkkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada

rindo = faz_me_rir_novamente('Fernanda')
print(rindo())

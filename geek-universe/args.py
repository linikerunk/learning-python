"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que vc poderá 
chamar de qualquer coisa, desde que começe com asterisco.

Exemplo 
*xis

Mas por convenção, utilizamos *args para definilo

Mas o que é o *args?

O Parâmetro *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla. Entao desde ja lembre-se que tuplas são imutaveis
"""

# Exemplos

# def soma_todos_numeros(num1=1, num2=2, num3=3):
#     return num1 + num2 + num3

# print(soma_todos_numeros(4, 5, 4))

# # print(soma_todos_numeros(4, 5))   num1=1, num2=2 ajustamos o typeerror
# # print(soma_todos_numeros(4, 5, 6, 7)) TypeError


# Entendendo o args

def soma_todos_numeros(nome, email, *args):
    return sum(args)
    # total = 0
    # for num in args:
    #     total = total + num
    # return total

print(soma_todos_numeros("Angelina", "Jolie"))
print(soma_todos_numeros("Angelina", "Jolie", 1))
print(soma_todos_numeros("Angelina", "Jolie", 1, 2))
print(soma_todos_numeros("Angelina", "Jolie", 1, 2, 3))


# Outro exemplo de utilização de *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu nao tenho certeza de quem vc  é ...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))


def soma_todos_numeros(*args):
    print(args)
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1, 2, 3, 5, 7, 10))

numeros = [1, 1, 2, 3, 4, 4, 67]
num1, num2, num3, num4, num5, num6, num7 = numeros

# Desempacotador

print(soma_todos_numeros(num1, num2, num3, num4, num5, num6, num7))

print(soma_todos_numeros(*numeros)) # Aqui estou desempacotando a lista
# OBS: o asterisco serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma,ele saberá que precisa
# rá antes desempacotar esses dados



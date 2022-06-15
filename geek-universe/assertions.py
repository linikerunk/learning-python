"""
Assertions (Afirmações/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirma-
ções utilizadas nos teste.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do
tió AssertionError

# OBS : Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma
mensagem de erro personalizada/

# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso
não precisa ser exclusivamente nos teste.

# ALERTA: Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parâmetro -O, nenhum assertion será
validado. Ou seja, todas suas validações já eram.

"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b

# ret = soma_numeros_positivos(2, 4) #6
# ret = soma_numeros_positivos(2, 4) #6
# print(ret)

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente',
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'

comida = input("Informe a comida : ")

print(comer_fast_food(comida))

# def faca_algo_ruim(usuario):
#     assert usuario.e_admin, 'Somente administradores podem fazer coisas ruim!'
#     destroi_todo_o_sistema()
#     return 'Adeus'



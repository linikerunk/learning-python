"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome,
 ou seja, funções anonimas.
"""

# Funções em Python

# def function(x):
#     return 3 * x + 1

# print(function(4))
# print(function(7))


# Exemplo de expressão Lambda
lambda x: 3 * x + 1
# lambda -> paremetro da função : regra negocio

# E como utilizar a expressao Lambda?
calc = lambda x: 3 * x + 1 # Não é a forma que vc vê geralmente
print(calc(4))
print(calc(7))


# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo("  LIniker", "oLIVEIRA"))
print(nome_completo("  Jefferson            ", "AlMeIdA"))

# Em Funções Python podemos ter nenhuma ou várias entradas, Em Lambdas também

amar = lambda: 'Como não amar Python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1/ z)

# n = lambda x1, x2, ..., xn: <expressao>


print(amar())
print(uma(6))
print(duas(6, 7))
print(tres(3, 6, 9))

#OBS: Se passarmos mais argumentos do que parámetros esperados teremos TypeError


print('\n \n \n')

# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower(), reverse=True)

print(autores)

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = A* x **2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0)) # 0 é o X
print(teste(1))
print(teste(2))

# usamos lambda para ordenação e filtragem de dados mas nao só se limitão a isso

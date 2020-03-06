"""
Módulo Collections - Named Tuple

# Recap tupla
tupla = (1, 2, 3) or tupla = 1, 2, 3

print(tupla[1])

# Named Tuple -> Tupla Nomeada... // São tuplas diferenciadas, onde especificamos
um nome para a mesma e também parâmetros

# Importando

from collections import namedtuple

# precisamos definir o nome e parâmetros.

# Forma 1

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple(('cachorro'), ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca="Chow-Chow", nome="Ray")

print(ray)

# Acessando o dados

# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2
print(ray.idade) # idade
print(ray.raca) # raça
print(ray.nome) # nome


print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))

https://docs.python.org/3/library/collections.html#collections.namedtuple
"""



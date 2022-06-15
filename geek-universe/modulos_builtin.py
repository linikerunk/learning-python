"""
Trabalhando com Módulos Builtin (módulos integradas, que já vem instalados no Python)
________________________
|Python|Modulos builtin|
|______________________|
"""

# utilizando alias (apelidos) para módulos/funções

import random as rdm

print(rdm.random())

# Podemos importar todas as funções as funções de um módulo utilizando o *

from random import *
# import random

print(random())

# importando todo o módulo 
# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

# import random 
# print(random.random())

# Utilizando alias (apelidos)
from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(7, 17))
lista = ['liniker', 'oliveira', 'jardel']
shuffle(lista)
print(lista)
print(choice("123456789"))

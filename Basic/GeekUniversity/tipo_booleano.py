"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

Errado:
true, false

Certo:
True, False
"""


ativo = True

print(ativo)

"""
Operações Básicas:
"""


# Negação (not):

"""
Fazendo  a negação, se o valor booleano for verdadeiro o resultado será falso,
se o valor for false o resultado se´ra verdadeiro, sempre ao contrário...
"""
print(not ativo)

logado = False

#Ou (or):
"""
E uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve
ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""

print(ativo or logado)


# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos devem 
ser valores verdadeiros.

True and True -> True;
True and False -> False;
False and True -> False;
False and False -> False;
"""

type(False)
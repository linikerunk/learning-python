"""
Módulo COllections - Counter (contador)

Além das collections built-in temos o modulo collections

Collection -> High-Performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections
Counter que é parecido com um dicionário como chave o leemento da lista passada como
parâmetro e como valor a quantidade de ocorrências desse elemento.


# Exemplo 1
# Utilizando o Counter

from collections import Counter # Realizando o import


lista = [1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 95, 32, 1, 2, 2, 2, 2]

# Utilizando o Counter // vou guardar em res para ver o retorno do método..

res = Counter(lista) # Counter conta quantas ocorrencias  existem na minha lista

print(type(res))
print(res)



# Exemplo 2
from collections import Counter

print(Counter("Geek University"))
# out : Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3
# Qual a palavra  que mais aparece no texto..

from collections import Counter

texto = "
The dead speak! The galaxy has heard a mysterious broadcast, a threat of REVENGE
in the sinister voice of the late EMPEROR PALPATINE.GENERAL LEIA ORGANA
dispatches secret agents to gather intelligence, while REY, the last hope of the
Jedi, trains for battle against the diabolical FIRST ORDER.Meanwhile, Supreme
Leader KYLO REN rages in search of the phantom Emperor, determined to destroy 
any threat to his power....
"

palavras = texto.split()
# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))


#Documentação da biblioteca..
www.docs.python.org/3/library/collections

################################################################################
"""


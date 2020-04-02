"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. 
o sort() so funciona em listas.

Podemos utilizar o sorted() com qualquer iterável

Como o próprio nome diz. sorted() serve para ordenar.
"""

tupla = 7, 2, 3

# print(tupla.sort()) # erro de atributo

print(sorted(tupla)) # sorted retorna uma nova lista a original se matém intacta...
print(tupla)

# Adicionando parâmetros ao sorted()
numeros = [1, 4, 5, 7, 2, 3]

print(sorted(numeros, reverse=True))# Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas
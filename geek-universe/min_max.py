"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos
"""

# Exemplos

lista = [15, 12, 23, 44, 53, 139]
print(max(lista))


tupla = (15, 12, 23, 44, 53, 139)
print(max(tupla))


conjunto = {15, 12, 23, 44, 53, 139}
print(max(conjunto))

dicionario = {'a': 15, 'b': 12, 'c': 23, 'd': 44, 'e': 53, 'f': 139}
print(max(dicionario))

dicionario = {'a': 15, 'b': 12, 'c': 23, 'd': 44, 'e': 53, 'f': 139}
print(max(dicionario.values()))

print(max(3, 44))

# Faça um programa que receba dois valores do usuário e mostre o maior valor

val1 = 42
val2 = 32

print(max(val1, val2))

print(max('a', 'b', 'g'))
print(max(1, 2, 3, 55, 14, 10, 100))
print(max("Liniker"))


#min() -> Retorna todos menor valor do conjunto...
val1 = 42
val2 = 32

print(min(val1, val2))

print(min('a', 'b', 'g'))
print(min(1, 2, 3, 55, 14, 10, 100))
print(min("Liniker"))


# Outros exemplos 

nomes = ["Guilherme", "Rafael", "Dora", "Oliveira", "Tim"]

print(max(nomes)) # vai pegar a maior palavra[0] 
print(min(nomes)) # vai pegar o menor palavra[0]

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))


musicas = [
    {'titulo': "Thunderstruck", "tocou": 3},
    {'titulo': "Nothing else matters", "tocou": 6},
    {'titulo': "Insdestructible", "tocou": 1},
    {'titulo': "November Rain", "tocou": 2},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO: Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])


# DESAFIO: Como encontrar a música mais tocada sem usar max min e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max=musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 999999
for musica in musicas:
    if musica['tocou'] < min:
        min=musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
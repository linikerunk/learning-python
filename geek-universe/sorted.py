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


usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Bob", "tweets": ["So jogo video-game", "Dormo 3 horas por dia"]},
    {"username": "Carla", "tweets": ["Odeio meus irmãos"], "cor": "Amarelo"},
    {"username": "Rafaela", "tweets": ["Passei em primeiro no Enem", "Bio-Ciência"]},
    {"username": "Fernando", "tweets": []},
    {"username": "Liniker", "tweets": ["One piece é vida"], "cor": "perto", "musica": "Rock"}

]

# Ordenar pelo tamanho do dicionario
print(usuarios)
print(sorted(usuarios, key=lambda usuario : usuario['username'], reverse=True))

# Ordenando por número de tweets
print(" POR TWEETS \n")
print(sorted(usuarios, key=lambda usuario : len(usuario['tweets'])))


# Último exemplo

musicas = [
    {'titulo': "Thunderstruck", "tocou": 3},
    {'titulo': "Nothing else matters", "tocou": 6},
    {'titulo': "Insdestructible", "tocou": 1},
    {'titulo': "November Rain", "tocou": 2},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
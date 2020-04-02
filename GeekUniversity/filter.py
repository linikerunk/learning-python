"""
Filter

# utilizado para filtrar dados de uma determinada coleção...

Spotify filtrar musica para fazer um top 10 das mais tocadas.
"""

# valores = (1, 2, 3, 4, 5, 6)

# media = sum(valores)/ len(valores)

# print(media)

import statistics # serve para trabalhar com dados estatisticos...

# Dados coletados de algum sensor

dados = [1.3, 2.7, 8.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)
print(f'Media : {media}')

# OBS : Assim como a função map(), a filter() recebe dois parâmetros, sendo uma
# função e um iterável

result = filter(lambda valor: valor > media, dados)
print(type(result))
print(list(result))

print(f'Novamente : {list(result)} ')

#OBS : Assim como na função map(), após serem utilizados os dados de filter()
# eles são excluidos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

res = filter(lambda pais: len(pais) > 0, paises)

res = filter(lambda pais: pais != '', paises)

print(list(res))

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto 
# mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto
# filtrando apensa os elementos de acordo com a função

# filter sempre retorna True ou False
# map ele retorna valor..


# Exemplo mais complexo

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Bob", "tweets": ["So jogo video-game", "Dormo 3 horas por dia"]},
    {"username": "Carla", "tweets": ["Odeio meus irmãos"]},
    {"username": "Rafaela", "tweets": ["Passei em primeiro no Enem", "Bio-Ciência"]},
    {"username": "Fernando", "tweets": []},
    {"username": "Liniker", "tweets": ["One piece é vida"]}

]

#Filtrar os usuários que estão inátivos no tweeter...

print(usuarios)

#Forma 1
inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))

print(inativos)

#Forma 2
inativos = list(filter(lambda user: not user['tweets'], usuarios))

print(inativos)


# combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutura é' + nome, desde que cada nome
# tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutura é {nome}', filter(lambda nome: len(nome) <= 5, nomes)))

print(lista)
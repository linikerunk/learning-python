import requests

# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)


# Acessando os dados da resposta

print(avaliacoes.json())
print(type(avaliacoes.json()))

# Acessando as quantidades de registros

print(avaliacoes.json()['count'])

# Acessando a próxima página de resultado

# print(avaliacoes.json()['next'])
# avaliacoes_page_2 = requests.get(avaliacoes.json()['next'])
# print(avaliacoes_page_2.json())

# Acessando os resultados desta página

print(avaliacoes.json()['results'])
print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
print(avaliacoes.json()['results'][1])

# Acessando o ultimo elemento da lista de resultados
print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que fez a ultima avaliação
print(avaliacoes.json()['results'][-1]['nome'])


# GET Avaliacao

avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/7/')

print(avaliacao.json())

# GET Cursos

headers = {'Authorization': 'Token a09568b611aed14776e4e2036af78de136c94fa4'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())

import requests

headers = {'Authorization': 'Token a09568b611aed14776e4e2036af78de136c94fa4'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())

# Testando se o endpoint está correto.

assert resultado.status_code == 200

# Testando quantidades de registros

assert resultado.json()['count'] == 5

# Testando se o título do primeiro curso está correto
assert resultado.json()[
    'results'][0]['titulo'] == 'Programação para Web com Django Framework'

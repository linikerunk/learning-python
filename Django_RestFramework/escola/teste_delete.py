import requests

headers = {'Authorization': 'Token a09568b611aed14776e4e2036af78de136c94fa4'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando o código de status HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retorno é 0

assert len(resultado.text) == 0
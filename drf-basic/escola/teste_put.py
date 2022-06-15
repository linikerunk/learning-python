import requests

headers = {'Authorization': 'Token a09568b611aed14776e4e2036af78de136c94fa4'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo Curso de scrum 3 ",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

# Buscando o curso com id 6

# curso = requests.get(f'{url_base_cursos}6/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)


# Testando o código de status HTTP

assert resultado.status_code == 200
print(resultado.json()['titulo'])
print(curso_atualizado['titulo'])

# Testando o Título

assert resultado.json()['titulo'] == curso_atualizado['titulo']

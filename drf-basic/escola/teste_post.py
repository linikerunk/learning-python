import requests

headers = {'Authorization': 'Token a09568b611aed14776e4e2036af78de136c94fa4'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


novo_curso = {
    "titulo": "Gerência Ágil de Projetos com Scrum 2",
    "url": "http://www.geekuniversity.com.br/scrum2"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o código de status HTTP 201

assert resultado.status_code == 201

# Testand ose o título do curso retornado é o mesmo do informado

assert resultado.json()['titulo'] == novo_curso['titulo']
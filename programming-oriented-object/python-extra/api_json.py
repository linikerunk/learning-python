# Iremos usar api sobre filmes OMDb API
import requests
import json

req = None

try:
    req = requests.get("http://www.omdbapi.com/?apikey=61a4e9f0&y=2000")

except Exception as e:
    print("Erro na conexão : ", e)
    exit()

dicionario = json.loads(req.text)


print("Titulo:", dicionario['Title'])

print("Ano:", dicionario['Year'])

print("Diretor: ", dicionario['Director'])

print("Atores:", dicionario['Actors'])

import requests #Beautiful Soup 4 você consegue fazer WebScraping

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com'}
texto = None;

try:
    requisicao = requests.get('https://www.youtube.com.br/')
except Exception as e:
    print("Requisição falhou.. erro : ", e)

try:
    requisicao2 = requests.post(
        'https://putsreq.com/1ighX0Nq46pHIgTB2xeo', header=cabecalho)

    texto = requisicao2.text
except Exception as e:
    print("Requisição falhou.. erro : ", e)
#print(type(requisicao)) # Tipo Response para resposta

print(requisicao.status_code)# mostra o status da requisição
print(requisicao.text)# aqui traz o código fonte ...

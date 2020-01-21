#Cotação API https://economia.awesomeapi.com.br/all

import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/')

    cotacao = json.loads(requisicao.text)

    print("***********************************************************************")
    print("####COTACAO DOLLAR####", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('Valor do Real BRL (1R$): ')
    print('Dolar: ', cotacao['USD']['high'], "em reais.")
    print('Dolar Canadense: ', cotacao['CAD']['high'], "em reais.")
    print('Euro: ', cotacao['EUR']['high'], "em reais.")
    print('Libra: ', cotacao['GBP']['high'], "em reais.")
    print('Peso Argentino: ', cotacao['ARS']['high'], "em reais.")
    print('BitCoin: ', cotacao['BTC']['high'], "em reais.")
    print("***********************************************************************")
    time.sleep(2)

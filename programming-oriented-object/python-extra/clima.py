import requests
import json

cidade = input("Escreva sua cidade : \n ")

requisicao = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?q="+cidade+'&appid=b581d59fa511fdf958d9e25b6e22957c')

tempo = json.loads(requisicao.text)

print('Condição do tempo: ', tempo['weather'][0]['main']) 
print('Temperatura de : ', round(tempo['main']['temp'] - 273.15),'ºC')
print('Máxima de : ', round(tempo['main']['temp_max'] - 273.15),'ºC')
print('Mínima de : ', round(tempo['main']['temp_min'] - 273.15),'ºC')


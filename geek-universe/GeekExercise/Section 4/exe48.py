"""
Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

tempo = input("Digite quantos segundos : ")
try:
    tempo = int(tempo)
    horas = (tempo / 3600)
    minutos = (tempo - (horas * 3600))/60
    segundos = (tempo - (horas * 3600)- (minutos * 60)) 
    print(f'Valor em Horas : {int(horas)} : {int(minutos)} : {int(segundos)}')
except:
    print("Digito inválido")
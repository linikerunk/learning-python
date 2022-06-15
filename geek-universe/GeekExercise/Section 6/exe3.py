"""
Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva 
na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagme "FIM"! após a 
contagem.
"""
import time

print("Cotagem regressiva...")

cont = 10

while int(cont) != -1:
    print(cont)
    if cont == 0:
        print("FIM!")
    cont -= 1
    time.sleep(1)
    
"""
Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é
K = 1.61 * M, sendo K a distância em quilômetros e M em milhas
"""

milhas = ''
while type(milhas) != float:
    milhas = input("Digite uma distância em milhas : ")
    try:
        milhas = float(milhas)
        break
    except:
        print("Digite um número")
print(f'{milhas} em Milhas e igual à {round((1.61 * milhas ),2)} Quilômetros.')
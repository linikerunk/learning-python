"""
Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de conversão é M = K/1.61,
Sendo K a distância em quilômetro e M em milhas
"""

quilometros = ''
while type(quilometros) != float:
    quilometros = input("Digite uma distância em Quilômetros: ")
    try:
        quilometros = float(quilometros)
        break
    except:
        print("Precisa ser um números")
print(f'{quilometros} em Quilômetros e igual à {round(( quilometros / 1.61), 2)} em Milhas')


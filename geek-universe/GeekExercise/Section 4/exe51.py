"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0, 0)
"""
import math

while True:
    x = input("Digite o valor da coordenada X : ")
    y = input("Digite o valor da coordenada Y : ")

    try:
        x = float(x); y = float(y)
    except:
        print("Valor inválido.")
    
    result = math.sqrt((x ** 2) + (y ** 2))
    print(f'A distancia da coordenada X:{x}, Y:{y} é igual a : {round(result, 2)}')
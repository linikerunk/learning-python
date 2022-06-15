"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""

polegadas = None
while not polegadas:
    polegadas = input(" Digite um valor em polegadas : ")
    if not polegadas.isdigit():
        polegadas = input(" Digite um NUMERO em polegadas : ")
    else:
        polegadas = float(polegadas)
        break

centimetros = ( polegadas * 2.54 )

print(f"{polegadas} polegadas convertida para centimetros é igual a : {round(centimetros, 2)} cm")

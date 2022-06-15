"""
Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é  P = (C / 2.54), sendo C o comprimento em centímentros e P
o comprimento em polegadas.
"""


centimetros = None
while not centimetros:
    centimetros = input(" Digite um valor em centimetros : ")
    if not centimetros.isdigit():
        centimetros = input( " Digite um NUMERO em centimetros : ")
    else:
        centimetros = float(centimetros)
        break
polegadas = ( centimetros / 2.54 )
print(f"{centimetros} cm convertido em polegadas é igual a : {round(polegadas, 2)}")

"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é : M = H * 10000, sendo M a área em metros quadrados e H
a área em hectares.
"""

hectares = float(input("Digite um valor em hectares : "))
metros_quadrado = float(hectares * 10000)
print(f"{hectares} Hectares equivalem : {round(metros_quadrado, 2)} m²")

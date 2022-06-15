"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A formulá de conversão é H = M * 0.0001, sendo M a área em metros quadrados e H
a áreas em hectares.
"""

metros_quadrados = input("Digite um valor em metros quadrados : ")
print(f"{metros_quadrados} m² equivalem {round((float(metros_quadrados) * 0.0001), 4)} hectares. ")
"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é
M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
"""

while True:
    jardas = input("Digite um valor em Jardas : ")
    try:
        jardas = float(jardas)
        metros = ( jardas * 0.91 )
        conversao = round(metros, 2)
        print(f"{jardas} Jardas convertida em metros é igual a : {conversao}")
        # Deixar em loop para testar outros...
    except:
        print("Valor precisa ser válido.")
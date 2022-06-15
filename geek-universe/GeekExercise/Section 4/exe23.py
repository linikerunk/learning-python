"""
Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula  de conversão é
J = ( M / 0.91 ), sendo J o comprimento em jardas e M o comprimento em metros.
"""

while True:
    metros = input("Digite o valor em metros : ")
    try:
        metros = float(metros)
        jardas = ( metros / 0.91 )
        print(f"{metros} em Metros convertido em Jardas é igual a : {round(jardas, 2)}")
    except:
        print("Valor inválido, favor digitar um valor válido.")
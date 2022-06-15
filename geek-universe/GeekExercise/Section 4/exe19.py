"""
Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. a fórmula de conversão 
é M = (L / 1000), sendo L o volume em litros e M o volume em metros cúbicos.
"""

while True:
    litros = input("Digite o volume em Litros : ")
    try:
        litros = float(litros)
        conversao = ( litros / 1000 )
        print(f"{litros} Litros para m³ : {round(conversao, 4)}")
        break
    except:
        print("Oops!  Erro no número, digite um valor válido.")

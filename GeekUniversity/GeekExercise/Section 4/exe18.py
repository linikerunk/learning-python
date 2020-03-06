"""
Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. a fórmula de conversão é:
L = 1000 * M, sendo L o volume em litros e M o volume em metros cúbicos.
"""

while True:
    metros_cubicos = input("Digite o volume em m³ : ")
    try:
        metros_cubicos = float(metros_cubicos)
        conversao = ( 1000 * metros_cubicos )
        print(f"{metros_cubicos} m³ para Litros : {round(conversao, 2)}")
        break
    except:
        print("Oops!  Erro no número, digite um valor válido.")


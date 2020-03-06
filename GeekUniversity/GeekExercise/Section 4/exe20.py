"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de
conversão é L = (K / 0.45), sendo K a massa em quilogramas e L a massa em libras.
"""

while True:
    quilogramas = input("Digite o valor da massa em quilogramas : ")
    try:
        quilogramas = float(quilogramas)
        libras = ( quilogramas / 0.454 )
        print(f"{quilogramas} quilogramas convertido em Libras é igual a : {round(libras, 2)}")
        break
    except:
        print("Digite um valor válido.")
    

    
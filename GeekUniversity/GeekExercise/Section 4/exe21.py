"""
Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é K = L * 0.45,
sendo K a massa em quilogramas e L a massa em libras. 
"""

while True:
    libras = input("Digite o valor da massa em libras : ")
    try:
        libras = float(libras)
        quilogramas  = ( libras * 0.453 )
        print(f"{libras} libras convertido em Quilogramas é igual a : {round(quilogramas, 2)}")
        break
    except:
        print("Digite um valor válido.")
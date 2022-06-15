"""
Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
"""

while True:
    print("Digite o tamanho do lado do quadrado : ")
    try:
        lado = input()
        lado = float(lado)
        print(f"Valor da área do quadrado : {lado * lado}")
    except:
        print("Valor Inválido.")
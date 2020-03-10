"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

while True:
    digito = input("Digite um valor positivo : ")
    try:
        digito = float(digito)
        if digito >= 0:
            print(f"O digito {digito} é válido pois é positivo.")
        else:
            print("Digito inválido pois não é positivo.")
    except:
        print("Precisa ser um número : ")
    

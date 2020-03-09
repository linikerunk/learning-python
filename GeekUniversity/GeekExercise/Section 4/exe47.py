"""
Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima um digito por linha.
"""

while True:
    numero = input("Digite um número : ")  
    try:
        numero = int(numero)
        if numero > 9999 or numero < 1000:
            print("Número deve ter entre 0 a 4 digitos.")
        else:
            for digito in str(numero):
                print(digito)
    except:  
        print("Digito inválido.")
    
            
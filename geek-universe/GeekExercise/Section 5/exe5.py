"""
Faça um número que reeba um número inteiro e verifique se este número é par
ou impar.
"""

while True:
    numero = input("Digite um número : ")
    try:
        numero = float(numero)
    except:
        print("Digito inválido")
    finally:
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é impar.")
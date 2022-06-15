"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""

while True:
    try:
        numero = input("Digite um número inteiro : ")
        numero = int(numero)

        soma_sucessor = ((numero * 3) +1) + ((numero * 2) - 1)
        print(f"soma do sucessor de seu triplo com o antecessor de seu dobro : {soma_sucessor}")
    except:
        print("Valor inválido...") 
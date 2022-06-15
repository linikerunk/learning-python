"""
Leia um número inteiro e imprima o seu antecessor e o seu sucessor.

"""

while True:
    numero = input("Digite um número inteiro :")

    try:
        numero = int(numero)
        print(f" Antecessor : {numero - 1}")
        print(f" Sucessor : {numero + 1}")
        continuar = input("Deseja ver outro número: [SIM] [NAO] : ")
        continuar = continuar.upper()
        if continuar == "SIM":
            continue
        elif continuar == "NAO":
            print("Adeus!!")
        else:
            print("Digito inválido.")

    except:
        print("Valor digitado inválido")

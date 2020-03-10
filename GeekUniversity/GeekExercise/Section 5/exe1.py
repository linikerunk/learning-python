"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""

numeros = []

while True:
    num = input("Digite um número ou [SAIR] para sair : ")
    try:
        if num == 'SAIR' or num == 'sair':
            print("Saindo...")
            break;
        else:
            num = float(num)
            print(num)
            numeros.append(num)
            print(numeros)
            continuar = input("Deseja adicionar outro número [SIM] / [NAO] : ")
            continuar = continuar.upper()
            print(continuar)
            if continuar == 'SIM':
                pass
            elif continuar == 'NAO':
                print(f"O maior valor dos elementos da lista é : {max(numeros)}")
                break;
            else:
                print("Apenas [SIM] ou [NAO].")
                break;
    except:
        print("Digito inválido")
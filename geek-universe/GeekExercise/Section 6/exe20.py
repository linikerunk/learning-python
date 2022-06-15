"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não.
Deverá ser informado o número de dados lidos e números de valores pares. O pro-
cesso termina quando for digitado o número 1000.
"""
counter_pair = []
while True:
    sequency = input("Digite um número ou 1000 para sair : ")
    try:
        sequency = int(sequency)
    except:
        print("Digito inválido.")
    finally:
        if sequency == 1000:
            print("Obrigado, programa está finalizando.")
            break
        elif sequency % 2 == 0:
            print(f"O número {sequency} é par.")
            counter_pair.append(sequency)
        else:
            print(f"O número {sequency} não é par.")

    print(f"Todos os números pares são : {counter_pair}")


"""
Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""

while True:
    digit = input("Digite um número para verificar seus divisores : ")
    try:
        digit = float(digit)
    except:
        print("Digito inválido")
    finally:
        # for num in range(1, int(digit)+1):
        #     if num % 2 == 0:
        #         print(num)
        #         if num % digit == 0:
        #             print(f"{num} é um divisor de {digit}")
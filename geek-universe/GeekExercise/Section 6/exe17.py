"""
Faça um programa que leia um número inteiro positivo N e calcule a soma dos n 
primeiros números naturais.
"""

while True:
    sum_of_number = 0
    number = input("Digite um número inteiro positivo : ")
    try:
        number = int(number)
    except:
        print("Digito inválido")
    finally:
        if number < 0:
            print("Número deve ser positivo")
        else:
            for num in range(0, number+1):
                sum_of_number = sum_of_number + num
    print(f"Da soma dos N números naturais calculado : {sum_of_number}")
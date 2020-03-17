"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles
e quantas vezes o maior números foi lido. A quantidade de números a serem lidos
deve ser fornecidade pelo usuário.
"""

quantity = input("Digite a quantidade de números que quer verificar : ")
numbers = []; maximum = 0; time_of_maximum = 0
try:
    quantity = int(quantity)
except:
    print("Digito inválido.")
finally:
    for num in range(0, quantity):
        num = input("Digite um número inteiro : ")
        try:
            num = int(num)
        except:
            print("Digito inválido.")
        numbers.append(num)
    maximum = max(numbers)
    time_of_maximum = numbers.count(maximum)
    print(f"O maior número é : {maximum}.")
    print(f"Este número apareceu : {time_of_maximum} vezes.")
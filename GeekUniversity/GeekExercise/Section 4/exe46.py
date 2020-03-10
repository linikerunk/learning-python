"""
Faça um programa que leia um número inteiro positivo de três digitos ( de 100 a 
999) Gere outro número formado pelo dígitos invertidos do número lido. Exemplo :
número lido = 123, numero gerado = 321.
"""

numero = input("Digite o número : ")
numero = str(numero[::-1])
print(f'O número invertido é {numero}')

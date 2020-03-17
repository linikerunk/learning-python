"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior
valor lido.
"""

numbers = []
counter = 0

while counter < 10:
    number = input("Digite um número : ")
    try:
        number = float(number)
    except:
        print("Digito inválido.")
    numbers.append(number)
    counter = counter + 1
    print(numbers)

print(f"O Maior numero é : {max(numbers)}")
print(f"O Menor numero é : {min(numbers)}")


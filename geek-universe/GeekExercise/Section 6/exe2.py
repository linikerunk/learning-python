"""
Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A pri
meira ez deve usar a estrutura de repetição FOR, a segunda While, e a terceira
do while
"""

for number in range(1, 101):
    print(number)

number = 1
while number <= 100:
    print(number)
    number += 1

number = 1

while True:
    print(number)
    number = number + 1
    if(number > 100):
        break
"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.
"""

fahrenheit = float(input("Digite uma temperatura em Fahrenheit (Fº) : "))

celsius =  (5.0 * (fahrenheit - 32.0)/9.0) 

print(f'A temperatura {fahrenheit} em Fahrenheit para Celsius é {celsius} (Cº)')
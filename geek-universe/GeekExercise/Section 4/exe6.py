"""
Leia uma temperatura em graus Celsius e apresente-a convertuda em graus Fahrenheit.
A fórmula de conversão é : F = C *(9.0/5.0) + 32.0, Sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius
"""

celsius = float(input("Digite uma temperatura em Celsius (Cº) : "))

fahrenheit = round((celsius * (9.0/5.0) + 32.0), 2)

print(f'A temperatura {celsius} em Celsius para Fahrenheit é {fahrenheit} (Fº)')
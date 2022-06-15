"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
fórmula de conversão é: C = K - 273.15,  sendo C a temperatura em Celsius
e K a temperatura em Kelvin.
"""

kelvin = float(input("Digite uma temperatura em Kelvin (Kº) : "))

celsius = round((kelvin - 273.15), 2)

print(f'A temperatura {kelvin} em Kelvin para Celsius é {celsius} (Cº)')
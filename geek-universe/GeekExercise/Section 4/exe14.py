"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * pi/180, sendo G o ângulo em graus e R em radianos e PI = 3.14
"""

PI = 3.14159265358979

angulo = int(input("Digite o valor do grau do ângulo : "))
print(f"O valor do ângulo de {angulo} convertido em radianos é : {round(((angulo * PI)/180),2)}")

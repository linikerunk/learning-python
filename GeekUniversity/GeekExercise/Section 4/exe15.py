"""
Leia um ângulo em radianos e apresente-o convertido em graus, a fórmula de conversão é
G = R * 180/PI, sendo G o ângulo em graus e R em radianos e PI = 3.14
"""
PI = 3.14159265358979

radianos = float(input("Digite o valor do ângulo em radianos : "))
print(f"O valor do ângulo de {radianos} em radianos convertido em Graus é : {round(radianos * (180 / PI), 2)}")
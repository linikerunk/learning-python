"""
Leia uma velocidade em km/h e apresente-a convertidade em m/s. A fórmula de con-
versão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.
"""

quilometro_horas = ''
while type(quilometro_horas) != float:
    quilometro_horas = input("Digite uma velocidade em Km/h : ")
    try:
        quilometro_horas = float(quilometro_horas)
        break
    except:
        print("Digite um número.")

print(f"{quilometro_horas} Km/h é igual a {round((quilometro_horas/3.6), 2)} M/s")
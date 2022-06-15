"""
Leia uma velocidade em m/s a apresente-a convertida em km/h. A fórmula de conversão é K: M * 3.6, sendo K
a velocidade em km/h e M em m/s.
"""

metros_horas = ''
while type(metros_horas) != float:
    metros_horas = input("Digite uma velocidade em metros por segundos m/s : ")
    try:
        metros_horas = float(metros_horas)
        break
    except:
        print("Digite um número")
print(f'{metros_horas} M/s é igual a {round((metros_horas * 3.6),2)} Km/h')

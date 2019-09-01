#Escreva um programa que converta uma temperatura digitada em oC para
#oF. A fórmula para essa conversão é:



celsius = float(input('Digite a temperatura em Celsius: '))
cel_to_fah = float(((9 / 5) * celsius) + 32)

print(f'A temperatura {celsius} Cº para Farenheit é igual a : {cel_to_fah:.2f}')
"""
Leia um vakir en reak e a cotação do dólar. Em seguida, 
imprima o valor correspondente em dólares.
"""
print("Digite um valor em Real R$: ")
real = input()
try:
    real = float(real)
except:
    print("Valor inválido.")

print(" Cotação do Dollar em 06/03/2020  == 4,65")
dolar = (real * 4.65)

print(f'Seu valor em real é {real} convertido em Dolar $ é igual a {round(dolar, 2)}')
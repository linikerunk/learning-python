#Faça um programa que receba um número e 
# mostre uma mensagem caso este número seja maior que 10. 

numero = round(float(input(" Digite um número : ")),1)
if numero > 10: print(f"O Número {numero::.2f} é maior que 10.")
elif numero == 10: print(f"O Número {numero:.2f} é igual a 10.")
else: print(f"O Número {numero:.2f} é menor que 10.")


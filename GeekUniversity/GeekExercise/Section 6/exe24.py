"""
Escreva um programa que leia um número inteiro e calcule a soma de todos os 
divisores desse número, com exceção dele próprio. Ex: a soma dos divisores do
número 66 é  1 + 2 + 3 + 6 + 11 + 22 + 33 = 78 
"""

def dividers(num):
	for i in range(1, int(num)//2+1):
		if num % i == 0: 
		    yield i
 
num = input("Digite um número positivo : ")
try:
	num = float(num)
except:
	print("Digito Inválido.")
finally:
	if num < 0:
		print("Digito negativo não é válido.")
	else:
		 print("A soma dos divisores é : ", sum(list(dividers(num))))
        
        
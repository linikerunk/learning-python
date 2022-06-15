"""
Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""

# import numpy as np
# import time

def dividers(num):
	for i in range(1, int(num)//2+1):
		if num % i == 0: 
			yield i
	yield num
 
num = input("Digite um número positivo : ")
try:
	num = float(num)
except:
	print("Digito Inválido.")
finally:
	if num < 0:
		print("Digito negativo não é válido.")
	else:
		print(list(dividers(num)))
	
# print("Agora com Numpy, numero estático [10]")

# num_two = 10

# def divisores(num):
# 	n = np.arange(1, num)
# 	d = num % n
# 	zeros = d == 0
# 	print (n[zeros])
# divisores(num_two)
"""
Faça um programa que leia três números inteiros positivos e efetue o cálculo
de uma das seguintes médias de acordo com um valor numérico digitado pelo usua-
rio.
"""

# # from functools import reduce # Valid in Python 2.6+, required in Python 3
# # import operator
# import numpy as np

# while True:
#     def average_geometric(*numbers):
#         average = np.array(numbers)
#         return average.prod() ** (1.0/len(average))
       

#     def average_weighted(*numbers):
#         weight = []
#         while len(weight) < 3:
#             items = input("Digite o peso de cada nota em sequência : ")
#             weight.append(items)
        
#         for index in range(0, 3):
#             print("peso : ", weight[index])
#             print("Index : ", numbers[index])
#         #     numbers = float(index) * weight[index]
#         #     print(numbers)
#         # average = numbers / sum(weight)
#         # return average

#     def average_harmonica(*numbers):
#         average = len(numbers) / (1/numbers[1]) + (1/numbers[2]) + (1/numbers[3])
#         return average
        
#     def average_arithmetic(*numbers):
#         average = sum(numbers) / len(numbers)

#     try:
#         options = input("Digite uma opção válida \n \
#     1 - Média Geométrica : \n \
#     2 - Média Ponderada : \n \
#     3 - Média Harmônica : \n \
#     4 - Média Aritmética : ")
#         numbers = []
#         while len(numbers) < 3:
#             nums = input('Digite um número inteiro positivo : ')
#             nums = int(nums)
#             numbers.append(nums)
#     except:
#         print("Número inválido.")
#     if options == '1':
#         print(f"A Média Geométrica é {average_geometric(numbers)}")
#     elif options == '2':
#         print(f"A Média Ponderada é {average_weighted(numbers)}")
#     elif options == '3':
#         print(f"A Média Harmônica é {average_harmonica(numbers)}")
#     elif options == '4':
#         print(f"A Média Aritmética é {average_arithmetic(numbers)}")
#     else:
#         print("Opção inválida.")
"""
Faça um programa que receba três números e mostre-os em ordem crescente.
"""

numbers = []

while True:
    if len(numbers) < 3:
        nums = input("Digite um número : ")
        try:
            nums = float(nums)
        except:
            print("Digito Inválido.")
        finally:
            numbers.append(nums)
    else:
        print(f"Os números digitados ordenado na forma crescente é : {sorted(numbers)}")
        print(f"Os números digitados ordenado na forma decrescente é : {sorted(numbers, reverse=True)}")
        break

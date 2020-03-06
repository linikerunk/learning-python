"""
Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
"""
numeros = []
indice = 1
while (len(numeros) + 1)  < 4:
    print("Digite o ", indice, "número:")
    num = int(input())
    numeros.append(num)
    print(numeros)

print(f"A soma dos 3 números é : {sum(numeros)}")
"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lido

"""

numeros = []
while numeros != None:
    num = input("Digite um valor : ")
    try:
        num = float(num)
        numeros.append(num)
        if len(numeros) >= 3:
            break
    except:
        print("Digite um valor válido")

quadrados = [num**2 for num in numeros]
print(quadrados)
print(f"A soma dos  quadrados dos números passado foi {sum(quadrados)}")




"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os 
números pares de 0 até N em ordem decrescente
"""

while True:
    numbers = []
    number = input("Digite um número inteiro : ")
    try:
        number = int(number)
    except:
        print("Digito inválido")
    finally:
        if number % 2 != 0:
            print("Digito inválido, precisa ser um número par.")
            break
        else:
            for show in range(0, number+1, 1):
                if show % 2 != 0:
                    pass
                else:
                    numbers.append(show)
    print(list(reversed(numbers)))


# Podemos ter funções que são declaradas dentro de funções, e tábem tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

"""
Any e All

All() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda
se o iterável está vazio.

"""

# Exemplo All()

print(all([0, 1, 2, 3, 4])) # Todos os números são verdadeiros?
# o 0 é falso mas o retorno será False por conta do zero.

print(all([1, 2, 3, 5])) # Aqui é True..

print(all([]))

print(all((1, 2, 3, 5)))

print(all({1, 2, 3, 5}))

print(all("Liniker"))


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', "Cristina"]

print(all(nome[0] == 'C' for nome in nomes))

# OBS: Um iterável vázio convertido em boolean é False mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))


print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

# Any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável
# estiver vázio, retorna False

print(any([0, 1, 2, 3, 4])) # se algum elemento for True ele retorna True..

print(all([0, False, {}, (), []])) # False

print(any([nome[0] == "C" for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
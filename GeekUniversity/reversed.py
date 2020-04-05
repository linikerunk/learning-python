"""
Reversed

OBS : Não confunda com a função reserve() que estudamos da lista...

lista = [1, 2, 3, 4, 5]
lista.reverse()
5, 4, 3, 2, 1

nas tuplas nao existem reverse

# A função revesed() funciona com qualquer iterável, sua função é inverter o 
iterável.

"""
# A função reversed() retorna um iterável chamado List Reverse Iterator
# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter i elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Set conjunto
print(set(reversed(lista)))# não guardamos a ordem do set e por conta disso não existe o reversed

# Podemos iterar sobre o reversed

for letra in reversed('Geek University'):
    print(letra, end="")

# Podemos fazer o mesmo sem o uso do for
print("\n")
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais fácil com o slice de strings
print("Liniker"[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

print("\n range(9, -1, -1)")
# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)
"""
Teste de Velocidade que Expressão Geradoras

"""

# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num

gel = nums()

print(gel) # Generator

print(next(gel))
print(next(gel))

# Generator Expression

ge2 = (num for num in range(1, 10))

print(ge2) # Generation Expression

print(next(ge2))
print(next(ge2))

# Realizando o teste de velocidade

import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(1, 100000))) # 100 milhoes
gen_tempo = time.time() - gen_inicio


# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(1, 100000)]))
list_tempo = time.time() - list_inicio


print(f'Generator Expression levou {gen_tempo} \n \
List Comprehension levou {list_tempo} ')



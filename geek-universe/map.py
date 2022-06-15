"""
Map

# Mapeamento de função : valor
# Com map fazemos mapeamento de valores para função
"""

import math

def area(r):
    """Calcula a área de um círculo com raio 'r' """
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios =[2, 4, 5, 66, 4.2, 0.7]

#Forma comum para fazer esse calculo
areas = []
for r in raios:
    areas.append((area(r)))
print(areas)

# Forma 2 - Map

#Map é uma função que recebe dois parâmetros: O primeiro a função o Segundo um iterável.
# Retorna um Map Objecto

areas = map(area, raios)
print(areas)
print(type(areas))
print(tuple(areas))

# Geralmente passamos uma expressão lambda no map

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))
# OBS: após utilizarmos a função map, depois de usarmos a primeira utilização do
# resultado ele zerá.
# isso é interessante pq limpa a memória.

# Para fixar - Map

# Temos dados iteráveis:

# dados: a1, a2, ..., an

# Temos uma função:

# Função: f(x)

# Utilizamos a função ,ap(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função

# O Map Object: f(a1), f(a2), f(...), f(an)


# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27),
('New York', 28), ('Londres', 22)]

print(cidades)

# Precisamos converter de celsius para fahrenheit

# F = 9/5 * celsius + 32

# Lambda

c_para_f = lambda dado: (dado[0], round((9/5) * dado[1] + 32, 2))
print(list(map(c_para_f, cidades)))
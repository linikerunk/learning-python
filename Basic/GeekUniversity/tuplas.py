"""
Tupla (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla.

# print(type(())) # () isso é uma tupla

# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6, 7)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6, 7
print(tupla2)

print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tupla com 1 elemento

tupla3 = (4) # Isso não é uma tupla
print(tupla3)
print(type(tupla3))


tupla4 =(4, ) # Isso é uma tupla
print(tupla4)
print(type(tupla4))


tupla5 = 4, # Definimos o quê é tupla pela virgula
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírtula e não pelo uso do parênteses
s
(4) -> Não é tupla
(4, ) -> É tupla
4, -> É tupla

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ("Geek University", "Programação em Python: Essencial",)

escola, curso = tupla
print("Escola:", escola, "\nCurso:", curso)

# OBS: Gera erro (ValueError) se for número diferente de elementos para desempacotar.
# Métodos para: adição, remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6, 7, 'b')

# print(sum(tupla)) só se os válores forem inteiros
# print(max(tupla))
# print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 =(1, 2, 3)
print(tupla1)

tupla2 =(4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # Essa soma irá concatenar, Tuplas são imutáveis

print(tupla1)
print(tupla2)

# Para alterar uma tupla preciso criar uma nova tupla..
# tupla3 = tupla1 + tupla2

tupla1 = tupla1 + tupla2 # Ou sobrescevendo os valores..
print(tupla1)

tupla = 1, 2, 3

print(3 in tupla)

# Iterando sobre uma tupla

tupla = 1, 2, 3

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'f', 'a', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))


# Dicas na utilização de tuplas

# Devemos utilzar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante a de uma lista

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1


# verificamos em qual indice um elemento está na tupla

print(meses.index('Junho'))
# OBS: Caso o elemento não exista, será gerado ValueErro.


# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])


# Por que utilizar tuplas?
# - Tuplas são mais rápidas do que listas. IA, Performance.
# - Tuplas deixam seu código mais seguro*.

# * Isso porque trabalhar com elemento imutáveis traz segurança para o código.


# Copiando uma tupla para outra 

tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(tupla)

"""


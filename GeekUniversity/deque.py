"""
Módulo Collections - Deque
Podemos dizer que o deque é uma lista de alta performance.

"""

#import 
from collections import deque

# Criando deques

deq = deque('Liniker')

print(deq)

# Adicionando elementos no deque

deq.append('y')
print(deq)


# Isso já é uma diferença do deque para lista

deq.appendleft('k') # Adiciona no começo

print(deq)

# Removendo elementos
print(deq.pop()) # Aqui remove é retorna o ultimo elemento.
print(deq)

# Outra vantagem de usar o deque
print(deq.popleft()) # Remove e retorna o primeiro elemento

print(deq)

#https://docs.python.org/2/library/collections.html#collections.deque
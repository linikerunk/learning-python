"""
Entendendo Iterators e Iterables

Iterator ->
    -Um objeto que pode ter iterado.
    -Um objeto que retorna um dado, sendo um elemento por vez quando uma funçao
    next() e chamada:

Iterable ->
- Um objeto que irá retornar um iterator quando a função iter() for chamada.


"""

nome = 'Liniker' # ela pe um iteravel retorna um dado [l][i][n]
numeros = [1, 2, 3, 4, 5, 6, 7]

iter_nome = iter(nome)
iter_numeros = iter(numeros)

print(next(iter_nome))
print(next(iter_numeros))

for letra in nome:
    print(f'{letra}')
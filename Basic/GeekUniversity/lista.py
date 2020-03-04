"""
Lista 
Lista em Python funcional como vetores/matrizes  (arrays) em outras linguagens,
com a diferença de serem DINÁMICA e támbem de podermos colocar QUALQUER tipo de dado.


Linguagens C/Java:
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nesta linguagens se você criar um array do tipo int e com tamanho 5,
    esse array SEMPRE será do tipo inteiro e poderá ter sempre no máximo 5 valores.

Já em Python:
    - Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e 
    simplesmente ir adicionando elementos;
    - Qualquer tipo de dado: As listas não possuem tipo de dados fixos, ou seja
    podemos colocar quaisquer tipos de dados.

As lista em Python são representadas por colchetes: []



#Podemos facilmente checar se determinado valor está contido na lista

num = 18
if num in lista4:
    print(f'Na lista4 existe o número {num}')
else:
    print(f'O número {num} não existe nessa lista.')

# Podemos facilmente ordenar uma lista...
lista1.sort()
print(lista1)


# Podemos facilmente conta o numero de ocorrências de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))


print(lista1)
lista1.append(42) # Append para inserir elemento, 1 elemento por vez.
print(lista1)


# lista1.append(12, 34, 56) # Erro

lista1.append([8, 3, 1, 10])
print(lista1)

if [8, 3, 1, 10] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

lista1.extend([123, 44, 67]) # ele uni as lista, como como elemento único da lista

print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice

lista1.insert(2, 'Novo Valor') #[(0, 1), (1, 99), (2, 'novo valor')]
print(lista1)


"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University') # == lista2

# Podemos facilmente junta duas listas.

lista1 = lista1 + lista2  # == extends..

lista1.extend(lista2)
print(lista1)
print(lista1)

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])

lista6 = lista2.copy()
print(lista6)

print(len(lista6))
print(len(lista1))

print(lista5)
lista5.pop()
print(lista5)

#OBS: Se não houver elemento no index informado, haverá um erro

lista5.pop(2) # posso passar o index que quero remover
print(lista5)


# Podemos remover todos os elemento ( Zerar a lista )
print(lista5)
lista5.clear()
print(lista5)

# Repetindo elementos em uma lista..

nova = [1, 2, 3]
nova = nova * 3
print(nova)
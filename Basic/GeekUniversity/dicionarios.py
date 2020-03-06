"""
carrinho tupla after

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adcionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação..


# Métodos de dicionário

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# # Limpar o dicionário (Zerar os dados)

# d.clear()

# print(d)


# Copiando um dicionario para outro 

# Forma 1 # Deep Copy

novo = d.copy() 

print(novo)

novo['d'] = 4

print(d)
print(novo)


# Forma 2 # Shallow Copy

d = dict(a=1, b=2, c=3)

novo = d

print(novo)

novo['d'] = 4 

print(d)
print(novo)


# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))


usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))


# O método from keys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave
# o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)


"""


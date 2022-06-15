"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

(0, 1, 2)  -> Indice da chave ..
(1, 2, 3)  -> Valor que a chave contém.

# Dicionários são representados por chave {}.

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

    
# Forma 1 (Mais comum)
########################################################################
print(type({}))
########################################################################
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
########################################################################
print(paises)
print(type(paises))
########################################################################


# Forma 2 (Menos Usual)

paises = dict(br="Brasil", eua="Estados Unidos", py="Paraguai")

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'} # Maneira correta
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da memsma forma que list/tuplas

print(paises['br'])
print(paises['eua'])
# print(paises['ru'])

# OBS: Caso tentamos fazer uma acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru')) # Aqui ele irá retornar um valor do tipo Vázio...


pais = paises.get('py')

if pais:
    print(f"Encontrei o país {pais}")
else:
    print("Não encontrei o país")

pais = paises.get('py', "Não Encontrei..") # Colocar um padrão se não encontrar o primeiro
print(f'Encontrei o país {pais}')

# pais = paises.get('ru')
# Caso o  get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

# Busca são realizadas por Chaves mas não por valor  com o in...

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises) # Aqui vai dar False pois é um valor..

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean),
# inclusive lista, tupla, dicionário, como chaves de dicionários.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas são imutáveis.

localidades =  {
    (35.6895, 39.6917): "Escritório em Tókio",
    (40.7128, 74.0060): "Escritório em Nova York",
    (37.7749, 122.4194): "Escritório em São Paulo",
}
# tuplas são imutáveis por isso é legal usar ela como chaves...
# Latitude e Longitude
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 de adicionar um novo valor.. ( Mais Comum )

receita['abr'] = 350
print(receita)

# Forma 2 
novo_dado = {'mai': 500}

receita.update(novo_dado) # Posso fazer dessa maneira tbm : receita.update({'mai' : 500}) 

print(receita)

# Atualizando dados em um dicionário

# Forma 1 
receita['mai'] = 600 # Atualização de um valor via chave..
print(receita) 

# Forma 2

receita.update({'mai': 700})
print(receita)

# CONCLUSÃO 1: A Forma de adicionar novos elementos ou atualizar dados em um dicionário e da mesma maneira.
# CONCLUSÃO 2: Em dicionários, Não podemos ter chaves repetidas.

# Removendo dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)

# OBS 1: Remove o último elemento do dicionário, passando o elemento, e caso não encontre o elemento um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2 - Neste caso o valor removido não é retornado

del receita['fev']
print(receita)

del receita['fev']
# Se a chave não existir será gerado um KeyError

"""

# Imagine que você tenha um comercio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
"""
Carrinho de Compras:
    Produto 1:
        - Nome;
        - Quantidade;
        - Preço;
    Produto 2:
        - Nome;
        - Quantidade;
        - Preço;

"""


# 1 - Poderíamos utilizar uma Lista para isso? Sim
carrinho = []

produto1 =['Playstation 4', 1, 2000.00]
produto2 =['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# - Teriamos que saber qual é o indice de cada informação do produto.

# 2 - Poderíamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o indice de cada informação no produto.

# 3 - Poderíamos utilizar um Dicionário para isso? Sim

carrinho = []

produto1 = { 'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2000.00}
produto2 = { 'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
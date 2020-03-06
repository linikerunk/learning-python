"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a
Teoria de conjunto da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets..

Dito isso, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não
importamos com a ordenação deles. Quando não precisamos se preocupar com chaves,
valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
        - Um dicionario tem chave/valor;
        - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valore repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um vlaor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto


# Forma 2  - Mais comum

s = {1, 2, 3, 4, 5}
print(s)
print(type(s))

if 3 in s:
    print("Tem o 3")
else:
    print("Não tem o 3")

# Importante lembrar que, além não de termos valores duplicados, não temos ordem.

# Listas aceitam valores duplicados, então temos 10 elementos.

# Tuplas aceitam valores duplicados, então temos 10 elementos.

# Dicionários não aceitam chaves duplicadas então temos 8 elementos.

# Conjuntos não aceitam valores duplicados, então temos 8 elementos.

dados = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34

lista = list(dados)
tupla = tuple(dados)
dicionario = {}.fromkeys(dados, '__dict__')
conjunto = set(dados)

print(f'Lista: {lista} com {len(lista)} de elementos')
print(f'Tupla: {tupla} com {len(tupla)} de elementos')
print(f'Dicionário: {dicionario} com {len(dicionario)} de elementos')
print(f'Conjunto: {conjunto} com {len(conjunto)} de elementos')


# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados
# em Sets

s ={1, 'b', True, 354.55, 'Liniker'}

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)
    
# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou
# museu e os visitantes informam manualmente a cidade de onde vieram

# Nós adicionamos cada cidade de uma lista Pythonm já que em uma lista podemos
# adicionar novos elementos e ter repetições

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande',
'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja únicas temos.

# O que você faria? Faria um loop na lista..?

# Podemos usar o set para isso:

print(len(set(cidades)))


# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4) # Duplicidade não gera erro, simplismente é ignorado e não é adicionado
print(s)

s = {1, 2, 3}
# Forma 1:
s.remove(3)# Não é indice póis conjuntos não são indexados.
# s.remove(23) Caso o valor não seja encontrado, será gerado KeyErro

# Forma 2:
s.discard(22) # Não gera erro!
s.discard(2)

print(s)

# OBS: Nenhum valor é retornado no set



s = {1, 2, 3}


print(s)

# Copiando um conjunto para outro...

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# Remove todos elementos de um conjunto
s.clear()
print(s)


# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python tambem estudam Java.

# Precisamos gerar um conjuntos com nomes de estudantes únicos

# Forma 1 - Utilizando Union..

# unicos1 = estudantes_python.union(estudantes_java)
unicos1 = estudantes_java.union(estudantes_python) # Mesmo resultado 
print(unicos1)

# Forma 2 - Utilizando o Caracter pipe |

unicos2 = estudantes_python | estudantes_java
print("Forma 2 \n ", unicos2)


# Gerar um conjunto de estudantes que estão em ambos cursos

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes de um curso que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print("Alunos que não fazem Java: ", so_python)

so_java = estudantes_java.difference(estudantes_python)
print("Alunos que não fazem Python : ",so_java)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * se os valores forem todos inteiros ou reais

s ={1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""




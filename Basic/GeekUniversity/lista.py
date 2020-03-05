"""
Lista  (list)
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


lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University') # == lista2



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



# Podemos facilmente converter uma string para uma lista

# Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split() #  OBS Por Padrão, o split separa os elemento da lista pelo espaço entre elas.
print(curso)

# Exemplo 2
curso = "Programação,em,Python,Essencial"
print(curso)
curso = curso.split(',') # Posso passar o separador dele..
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Coloca o cifrão em cada string .
curso = "$".join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dados em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 54545457575757]
print(lista6)
print(type(lista6))


# Iterando sobre listas 

# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair : ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em lista

numeros = [1, 2, 3, 4, 5]
# Or

num1 = 1; num2 = 2; num3 =3
numeros2 =[num1, num2, num3]

# Fazemos acessos aos elementos de forma indexada

#           0           1       2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])
# Fazer acesso aos elementos de forma indexada inversa
print(cores[-1]) # branco
#print(cores[-5]) # Erro pois não existe o indece -5

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetios

lista = []
lista.append(42)
lista.append(42)
lista.append(2)
lista.append(2) 
print(lista)

# Outros métodos nã otão importantes mas támbem úteis

# Encontrar o indice de um elemento na lista

numeros =[5, 6, 7, 5, 8, 9, 10]

# Em qual indice está o valor 6?
print(numeros.index(6))

# Em qual indice da lista está o valor 9?
print(numeros.index(9))

# OBS: Caso não tenha esse elemento na lista será apresentado ValueErro.
# print(numeros.index(19))

print(numeros.index(5)) # Retorna o primeiro elemento encontrado..

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar...


print(numeros.index(5, 1)) # Encontra o indice do valor 5 apartir do indice 1

# Podemos fazer busca dentro de um range, inicio/fim

print(numeros.index(8, 2, 6))# Buscar o valor do indice 8 entre 2 e 6

# Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slide de lista com o parâmetro 'inicio'

lista =[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[::])# todos elementos
print(lista[0:10:2])
# Posso passar valores negativos
print(lista[-4:])
print(lista[:-4])
print(lista[1:3]) # Começa em 1, pega até o indice 3 - 1

# Invertendo valores em uma lista.

nomes =['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)


nomes= ["Liniker", "Oliveira"]

nomes.reverse()
print(nomes)

# Soma, Valor Máximo, Valor Mínimo, Tamanho

# * Se os valores forem todos inteiros ou reais.

lista = [0, 2, 3, 55, 5, 5]

print(sum(lista)) # Soma
print(max(lista)) # Máximo valor
print(min(lista)) # Mínimo valor
print(len(lista)) # Tamanho da lista


# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla= tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotaento de listas ...

lista = ['Gui', 'Pedro', 'Liniker']
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS : Se tivermos mais elementos para desempacotar do que variáveis para receber os valores, teremos ValueError


# Copiando uma lista para outra( Shallow, Copy e Deep Copy)

# Forma 1 Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)


# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente idependentes,
# ou seja, modificando uma lista, não afeta a outra. Isso em Python é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# OBS: Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para nova lista, mas após realizar modificação em uma lista,
# essa modificação se refletiu em ambas as listas.
# Isso em Python é Chamado de Shallow Copy

"""

"""
List Comprehension

- Utilizando  List Comprehension nós podemos gerar novas listas com dados proce-
ssados com dados processados a partir de outro iterável

# Sintaxe da List Comprehension

[ dado for dado in iterável ]

"""

# Exemplos
numeros = [1, 2, 3, 4, 5, 6]

resultado = [numero  * 10 for numero in numeros]

print(resultado)

# Para entender melhor o que está acontecendo devemos dividir a expressão em duas
# partes:
# - A primeira parte : for numero in numeros
# - A segunda parte : numero * 10

resultado = [numero  / 2 for numero in numeros]

print(resultado)


def funcao(valor):
    return valor * valor

resultado = [funcao(numero) for numero in numeros ]

print(resultado)


# List Comprehension Versus Loop:

numeros_dobrados = []

for numero in [1, 2, 3 ,4, 5]:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# List Comprehesion / fazendo o passo de cima tudo em uma única linha.
print([numero * 2 for numero in [1, 2, 3 ,4, 5]])


nome ="Liniker Oliveira"

print([letra.upper()for letra in nome])

# Exemplo 2

amigos = ["Pedro", "Guilherme", "Thiago", "Augusto"]

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

print([caixa_alta(amigo) for amigo in amigos])

# Exemplo 3

print([numero * 3] for numero in range(1, 10))

# Exemplo 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.114]])

# Exemplo 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])
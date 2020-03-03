"""
Estrutura de repetição.
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java

for(int i = 0; i < 10, i++){
    //execução do tipo..
}

Python

for item in interavel:
    //execução do loop;

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplo de iteráveis:
- String
    nome = "Geek University"

- Lista
    lista = [1, 2, 3, 5, 7, 9]

- Range
    numeros = range(1, 10)
"""
nome = "Geek University";
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

#Exemplo de for 1
for letra in nome:
    print(letra)

#Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

"""
range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1, 2, 3, 4, 5, 6, 7, 8, 9
"""
#Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)


# Acesso ao indice da lista..

for i, v in enumerate(nome):
    print(f"Indice:{i}, Valor:{v}")

for indice, letra in enumerate(nome):
    print(indice)

for valor in enumerate(nome): # Aqui o enumerate cria uma tupla para cada indice da string...
    print(valor)

for valor in enumerate(nome):
    print(valor[0]) # traz somente os indices....
    print(valor[1]) # traz somente as letras.....

qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f"Informe o {n}/{qtd} valor:"))
    soma = soma + num
    print(f'A Soma é {soma}')
    # print(f'Imprimindo {n}')

nome1 = 'Geek University'
for letra in nome1:
    print(letra, letra, end='', sep="-")# Imprimo cada um dos caracteres mas sem pular linhas, e o sep é para eu criar um separador..

print(nome1 * 3)
print(nome1 * 3)
print(nome1 * 3)


"""
Tabelas de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

# Original: U+1F30F
# Modificado U0001F30F

emoji = '\U0001F605'

for _ in range(3):
    for num in range(1, 11):
        print(emoji * num)
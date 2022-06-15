"""
Modulo Random e o que são modulos ?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui varias funções para geração de números pseudo-aleatórios.
"""

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1
import random

# random() -> Gera um número pseudo-aleatório entre 0 a 1 

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes,
# propriedades que estiverem dentro do módulo ficarão disponiveis (Ficaram em memoria)

# Não recomendado importar o módulo todo ...

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome
# pacote e o nome da função seprados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confunso,
# mas a função random() é apenas uma função dentro do módulo random

# Forma 2 chamando o  modulo

from random import random

for i in range(0, 10):
    print(random())

# uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos
from random import uniform
for i in range(10):
    print(uniform(3, 7)) # 7 não é incluído.

# randint() -> Gerar valores pseudo-aleatorio de um número inteiro..

# Gerador de apostas para a mega-sena

from random import randint

for i in range(6):
    print(randint(1, 61), end=", ")
print("\n")

# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice

jogadas = ['pedra', 'papel', 'tesoura'] 
print(f"sua jogada foi: {choice(jogadas)}")

# print(choice('Geek University'))


from random import shuffle

# shuffle() -> Tem a função de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

shuffle(cartas)

print(cartas.pop())
print(cartas)


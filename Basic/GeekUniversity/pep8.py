import this # easter egg  ( The Zen Of Python, it was wroten for a poetic person ... )

'''
PEP8 - Python Enhancement Proposals  --> Proposta de Aprimoramento do Python

Existem varias PEPS  

PEP0 - PEP1

PEP8 -> Como condificar melhor  Style Guide for Python Code...

-------------------------------------------------------------------------------------------------

PEP8 - Python Enhancement Proposals 

São propostas de melhorias para a linguagem Python

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;
    Exemplo:
        class CalculadoraCientifica:
            pass

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis
    Exemplo:
        def soma():
            pass

        def soma_dois():
            pass

[3] - Utilize 4 espaços para identação!
    if('a' == 'a'):
        <-4 espaços..

[4] - Linhas em branco;
    - Para definir uma classe tem que ser duas linhas em branco...
    - Separar funções e definições de classe com duas linhas em branco;
    - Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports
    - Imports devem ser sempre feitos em linhas separadas;
    
    # Import Errado
    import sys, os

    #Import Certo
    import sys
    import os

    #Não há problemas em utilizar:
    from types import StringType, ListType

    #Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

    from types import (
        StringType,
        ListType,
        SetType,
        OutroType
    )

    # Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
    antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruçõe
    #Não faça
    funcao( algo[ 1 ], { outro: 2 } )

    #Faça
    funcao(algo[1], {outro: 2})
    
    #Não faça:
    algo (1)

    #Faça:
    algo(1)

    #Não faça:
    dict ['chave'] = lista [indice]

    #Faça:
    dict['chave'] = lista[indice]

    #Não faça:
    x           = 1
    y           = 2
    variavel_longa = 5

    #Faça:
    x = 1
    y = 3
    variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
import this
.finalizo aqui <--

The Zen of Python

'''
'https://a.udemycdn.com/2018-12-26_22-17-16-5e257669bfbc114b533a5504fcc5eccd/original.pdf?nva=20200302225029&token=0bc0e6ed692ee260d75fe'



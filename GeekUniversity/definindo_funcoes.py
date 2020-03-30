"""
Definindo Funções 
- Funções são pequenos trechos de código que realizam tarefas especificas:
- Pode ou não receber entradas de dados e retornar uma saída de dados:
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma funçã oque realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a funçao seja simplificada.

Já utilizamos várias funções:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;

"""

# Exemlo de utilização de funções;

cores = ['verde', 'amarelo', 'azul', 'branco']

# utilizando a função integrada (Built-in) do Python print()

# print(cores)

curso = "Programação em Python"

# print(curso)

cores.append('roxo')

# print(cores)

# curso.append('MAIS DADOS') ## erro só podemos usar essa função em uma lista
# print(curso)

cores.clear() # depende da lista e nao recebe nenhum paramêtro.

# print(help(print))
# DRY - Don't Repeat Yourself . Não repita seu código.

# Mas então, como definir funções?

"""
Em Python, e forma geral de definir uma função é:

def nome_da_função(parametros_de_entradas):
    bloco_da_funcao


Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto. separado
por um underline (Snake Case):
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por
virgula, podendo ser opcionais ou não;
bloco_de_funcao -> também chamados de corpo da função ou implementação, é onde o
processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS : Veja que para definir uma função, utilizamos a palavra reservada 'def' 
informando ao Python que estamos definindo uma função. Tambem abrimos o bloco de
código com o já conhecido dois pontos:

"""


def diz_oi():
    print('oi')

"""
OBS:

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a ínica coisa que ela faz
e dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Chamada de execução
diz_oi()

"""
ATENÇÃO:
Nunca esqueça de utilizar o parênteses ao executar uma função;
"""

def cantar_parabens():
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print("Viva o aniversáriante!!")

cantar_parabens()

for n in range(5):
    print(n)
    cantar_parabens()

canta = cantar_parabens
# variável canta recebe a execução do método cantar parábens.

canta()
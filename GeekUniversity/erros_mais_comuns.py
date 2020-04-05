"""
Erros mais comuns em Python

Aprender a ver a saída de erro.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando  o Python encontra um erro de sintaxe. Ou seja, você
escreveu algo que o Python não reconhece como parte da linguagem.

Exemplo SyntaxError
a)
def funcao:
    print(something)..

b)
None = 1
def = 2

c)
return

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplo NameError

a)
printf('Liniker')
funcao()


3 - TypeError -> Ocorre quando uma função/operação/ação e aplicada a um tipo errado.

a)
print(len(5)) # número nao tem tamanho...

print("Liniker" + []) # Nao posso concatenar str com lista...


4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro
tipo de dado indexado utilizando um índice inválido.

a)
lista = ['Liniker']
print(lista[10])

5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe
um argumento com tipo correto mas valor inapropriado.

a)
print(int('Liniker')) # o casting vai dar erro value..

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não
existe.

a)
dic = {'nome': 'Sub-zero'}
print(dic['poder'])

7 - AtributeError -> Ocorre quando uma variável não tem um atributo/função.

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

8- IndentationError -> acontece quando não respeitamos a indentação python (4 espaços)

def nova():
print('oi')

"""





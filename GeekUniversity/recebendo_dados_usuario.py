"""
Recebendo dados do usuário..

input () -> Todo dado recebido via input é do tipo String..

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# Aspas duplas triplas -> """Angelina Jolie"""


# Entrada de dados
# print("Qual seu nome? ")
# nome = input()

nome = input("Qual seu nome?")

#Exemplo de print 'antigo' versão 2.x
# print('Seja bem-vindo(a) %s' % nome) # %s para String e o % para concatenar com a variável ...

# Exemplo de print moderno criado  versão 3.x
# print("Seja bem-vindo(a) {0}".format(nome))

# Exemplo de print mais atual...
print(f'Seja bem-vindo(a) {nome}')

# print("Qual sua idade? ")
# idade = input()

idade = int(input("Qual sua idade?"))

# Processamento


#Saída de dados
#Exemplo de print 'antigo' versão 2.x
# print("A %s tem %s anos" % (nome, idade)) # se tiver mais de uma variável é necessario passar dentro de um parametro.

# Exemplo de print moderno criado  versão 3.x
# print('A {0} tem {1} anos '.format(nome, idade))

# Exemplo de print mais atual...
print(f'{nome} tem {idade} anos')
print(f'{nome} nasceu em {2018 - int(idade)}') # fazendo o cast em idade

#dir(__builtins__)  builtins --> São recursos integrado da linguagens onde as palavras reservadas são feitas..



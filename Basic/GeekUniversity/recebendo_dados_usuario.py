"""
Recebendo dados do usuário..
"""
# Entrada de dados
print("Qual seu nome? ")
nome = input()

#Exemplo de print 'antigo' versão 2.x
# print('Seja bem-vindo(a) %s' % nome) # %s para String e o % para concatenar com a variável ...

# Exemplo de print moderno criado  versão 3.x
# print("Seja bem-vindo(a) {0}".format(nome))

# Exemplo de print mais atual...
print

print("Qual sua idade? ")
idade = input()
# Processamento


#Saída de dados
#Exemplo de print 'antigo' versão 2.x
# print("A %s tem %s anos" % (nome, idade)) # se tiver mais de uma variável é necessario passar dentro de um parametro.

# Exemplo de print moderno criado  versão 3.x
# print('A {0} tem {1} anos '.format(nome, idade))

#dir(__builtins__)  builtins --> São recursos integrado da linguagens onde as palavras reservadas são feitas..



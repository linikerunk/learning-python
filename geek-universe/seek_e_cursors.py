"""
Seek e Cursors

seek() -> utilizada para mover o cursor pelo arquivo

"""

arquivo = open(r'leitura_file/texto.txt', 'r')
print(arquivo.read())

# A função seek() ->  é utilizada para movimentação do cursor pelo arquivo,
# ela recebe um parametro de onde está o cursor..

# Movimentando o cursor pelo arquivo com a função seek();

arquivo.seek(0) # Volta o cursor para posição zero..

print(arquivo.read())

arquivo.seek(588) # Começar na posição 588

print(arquivo.read())

arquivo.seek(0)

# # readline() -> função que lê o arquivo linha a linha...

# print(arquivo.readline()) # Linha por Linha até terminar a linha..
# print(arquivo.readline())
# print(arquivo.readline())

ret = arquivo.readline()
print(type(ret))
print(ret.split(' '))


# readLines() -> Lê todas linhas 

print(arquivo.readlines())

print(f"Tamanho de linhas : {len(arquivo.readlines())}")

# OBS: Quando abrimos um arquivo com a função open() é criado uma conexão entre o
# arquivo no disco do computador e o nosso programa. Essa conexão é chamada de 
# streaming. Ao finalizar a leitura de um arquivo devemos fechar a conexão com
# a função close();

# Passos para se trabalhar com um arquivo;

"""
1 - Abrir o arquivo;

2 - Trabalhar com arquivo;

3 - Fechar o arquivo;
"""

# 1 - Abrir o arquivo;
arquivo = open(r'leitura_file/texto.txt', 'r')

# 2 - Trabalhar o arquivo;
print(arquivo.read())  # Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed) # Verifica se oarquivo está aberto ou fechado.

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos
#  no arquivo

print(arquivo.read(50))

"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita -sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo nao existir.
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização leitura e escrita

#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso
exista, o novo conteúdo será adicionado ao final, mantendo o arquivo anterior
sem alteração.

Meaning

'r' - open for reading (default)

'w' - open for writing, truncating the file first

'x' - open for exclusive creation, failing if the file already exists

'a' - open for writing, appending to the end of the file if it exists

'b' - binary mode

't' - text mode (default)

'+' - open for updating (reading and writing)
"""

try:
    with open(r"leitura_file/university.txt", 'x') as arquivo:
        arquivo.write("Teste de conteúdo \n ")
except FileExistsError:
    print('Arquivo já existente..')

# Exmeplo com 'a'
# with open('leitura_file/frutas.txt', 'a', encoding="UTF-8") as arquivo:
#     while True:
#         fruta = input("Informe uma fruta ou digite sair : ")
#         if fruta != 'sair':
#             arquivo.write(fruta)
#             arquivo.write('\n')
#         else:
#             break

with open('leitura_file/outro.txt', 'r+', encoding="UTF-8") as arquivo:
    # arquivo.seek(0) # não controlamos o cursor com o modo 'a'
    arquivo.seek(0)
    arquivo.write("\nTESTANDO PARA VER SE TA NO TOPO 1!\n")
    arquivo.seek(38)
    arquivo.write("\nTESTANDO PARA VER SE TA NO TOPO 2!\n")
    arquivo.seek(0)
    arquivo.write("\nTESTANDO PARA VER SE TA NO TOPO 3!\n")
    arquivo.seek(38)

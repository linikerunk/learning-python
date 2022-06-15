"""
StringIO

ATEÇÂO: Para ler ou escrever dados em arquivos do sistema operacional o software
precisa ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever o arquivo.

# cat no linux serve para ler arquivo

StringIO -> Utilizado para ler e criar arquivo em memória.

# Primeiro fazemso o import
"""

from io import StringIO

mensagem = "Está é apenas uma string normal.."

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vázio
# para inserimos texto depois

arquivo =  StringIO(mensagem)
#arquivo =  StringIO(mensagem) === arquivo open("nome", 'w)
# Agora tendo o arquivo podemos utilizar tudo que já sabemos..
print(arquivo.read())

# StringIO vc cria o arquivo na memória nao precisa do arquivo ...

# Escrevendo outros textos em memória.
arquivo.write(" Outro texto ")

arquivo.seek(0)

print(arquivo.read())
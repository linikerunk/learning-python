"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalemten siginifica 'abrir';

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos entao.

# http://docs.python.org/3/library/functions.html#open

# OBS : por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou entã teremos o erro FileNotFoundError

_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'

"""

# exemplo

arquivo = open(r'.\leitura_file\texto.txt', 'r') # mode = 'r' Read, encoding = UTF-8 assento

ret = arquivo.read()
print(type(ret))
print(ret)
print(ret.split("\n"))
print(len(ret))

# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos  utilizar a função read()

print(arquivo.read())

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

# A função read() lê todo o conteudo do arquivo.

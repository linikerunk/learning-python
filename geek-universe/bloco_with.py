"""
O bloco with

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
são fechados após o bloco with.
"""

with open(r'leitura_file/texto.txt', 'r') as arquivo:
    print(arquivo.readlines())
    print("Arquivo está fechado : ", arquivo.closed)
# não preciso fechar o arquivo pois o bloco with fecha os arquivos..

print("Arquivo está fechado : ", arquivo.closed)

arquivo = open('Read_Files\\arquivo.txt', 'r') # modo W - Write, cria o arquivo para inputar
                                     # modo r - para ler o arquivo todo ...
                                     # modo a - metodo de escrita adicionando elementos.
                                     # modo b - para abrir imagens, arquivos.exe [Bytes]

print(arquivo.read())

'''
for i in range(0, 100):
    arquivo.write(f"Eae pessoal, beleza?  vezes: {i} \n")
'''

'''
for linha in arquivo:
    print(linha)
'''

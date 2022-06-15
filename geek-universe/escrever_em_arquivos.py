"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. 
  Apenas ler, da mesma forma, se abrirmos um arquivo para escrita. não podemos lé-lo
# somente escrever nele.

# OBS : Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

a função write() recebe um string como parâmetro. Caso contrário teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo nao existeir ele será 
criado, caso ele já exista. o anteriror será apagado e um novo será criado. Dessa 
forma, todo o conteudo no arquvio anterior é perdido.
"""
# Exemplo de escrita - modo 'w' - write (escrita)

with open(r'leitura_file/novo.txt', 'w') as arquivo:
    arquivo.write('Escrevendo dados em arquivo é muito fácil \n')
    arquivo.write('Podemos colocar quantas linhas quisermos. \n')
    arquivo.write('Esta é a ultima linha. \n')

# Muito tranquilo


# outra maneira ñ pythonica

# arquivo = open('leitura_file/mais.txt', 'w')

# arquivo.write("Um texto qualquer \n")


with open('leitura_file/for.txt', 'w') as arquivo:
    arquivo.write("Liniker vc é lindaum \n" * 1000)

# Lendo dados e escrevendo 

with open('leitura_file/frutas.txt', 'w', encoding="UTF-8") as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite sair : ")
        if fruta != 'sair':
            arquivo.write(f'{fruta} \n')
            # arquivo.write("\n")
        else:
            break
"""
Sistema de arquivos - Manipulação


"""

# descobrindo se um arquivo ou diretorio existe! 
import os

# Arquivo
print(os.path.exists('deque.py')) # True
print(os.path.exists('naoexisto.py')) # False

# Diretório

# Paths relativos
print(os.path.exists('leitura_file')) # True
print(os.path.exists('oi/nao/existo'))  # False
print(os.path.exists('GeekExercise/Section 4'))  # True

# Path absolutos

print(os.path.exists("C:\\Users\\Liniker\\Desktop\\Learning-Python-Basic-To-Advanced\\Basic"))  # True
print(os.path.exists("C:\\Users\\Liniker\\Desktop\\asesadarnsdisasasadsadsa"))  # False



# Criando arquivos
import os

# # Forma 1
# open('leitura_file\\arquivo-test.txt', 'w').close()

# # Forma 2
# open('leitura_file\\arquivo-test2.txt', 'a').close()

# # Forma 3

# with open('leitura_file\\arquivo-test3', 'w') as arquivo:
#     pass


# OBS: criando arquivo via mknod() 
# os.mknod('arquivo-teste4.txt');

# os.mknod(r'C:\Users\Liniker\Desktop\Learning-Python-Basic-To-Advanced\GeekUniversity\teste_osmkd.txt');


# OBS : Criando diretorios via mkdir()

# os.mkdir('temp')


# Criando multi-diretórios (árvore de diretórios)

# os.makedirs('caminho completo', exist_ok=True) 


# # Renomear arquivo e diretórios..
# os.rename('temp', 'geek') # Renomeia a pasta


# OBS: Se e diretório que queremos renomear não estiver vazio, teremos um OSError

# Arquivos
# os.rename('geek/temp.txt', 'geek/pychar.txt')


# ATENÇÃO !! Tome cuidado com os comando de deleção, pois eles não iram para a
# lixeira, eles somem.

# Removem arquivos
# os.remove("geek/pychar.txt")

# Removendo Diretorios, nao podem estar com files dentro dele tem que estiver vázio
# os.rmdir('geek')
# os.rmdir('temp')

# Removendo uma árvore de diretórios
# for arquivo in os.scandir('geek2'):
#     if arquivo.is_file():
#         os.remove(arquivo.path)
#     if not arquivo.is_file():
#         os.rmdir(arquivo.path)

# Podemos remover uma árvore de diretórios vázios

# os.removedirs('geek2/')

# ATENÇÃO : Ao remover arquivos e diretórios com Python eles não vão para a lixeira.. Eles vão Embora!
# temos biblioteca que manda para lixeira (sendto2trash)

# Arquivos temporarios
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University \n')
    input()


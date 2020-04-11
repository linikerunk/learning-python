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

# Forma 1
open('leitura_file\\arquivo-test.txt', 'w').close()

# Forma 2
open('leitura_file\\arquivo-test2.txt', 'a').close()

# Forma 3

# with open('leitura_file\\arquivo-test3', 'w') as arquivo:
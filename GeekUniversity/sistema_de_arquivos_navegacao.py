"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos
importar e fazer uso do modulo os.

os -> Operating System - Sistema Operacional
"""

import os

# getcwd() -> pega o current work directory - diretorio de trabalho corrente

print(os.getcwd())# retorna  o path absoluto


# Para mudar o diretório, podemos utilizar o chdir()

# os.chdir('..') # voltando um diretorio...

# print(os.getcwd())

# os.chdir('..')

# print(os.getcwd())

# os.chdir('..')

# print(os.getcwd())

# os.chdir('..')

# print(os.getcwd())

# os.chdir('..')

# print(os.getcwd())

# os.chdir('..')

print(os.getcwd())


# Podemos verificar se um diretorio é relativo ou absuluto

print(os.path.isabs(r"C:\\Users\\Liniker\\Desktop\\Learning-Python-Basic-To-Advanced\\GeekUniversity"))

# Podemos identificar o sistema operacional com o módulo os

print(os.name)

# Podemos ter mais detalhes no sistema operacional
# print(os.uname) Linux
import sys
print(sys.platform)

print(os.getcwd())
res = os.path.join(os.getcwd(), 'GeekExercise', 'Section 4')

os.chdir(res)

print(os.getcwd())

# Veja que o os.path.join() reebe dois parâmetros, sendo o primeiro o diretorio
# atual e o segundo  o diretório que será juntado ao atual..

import os

# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir())
print(len(os.listdir()), " Itens nesse diretorio.")

print(os.listdir('C:\\Users\\Liniker\\Desktop\\'))

# Podemos listar os arquivos e diretorios com mais detalhes com scandir()

# dentro do list
scanner = os.scandir('C:\\Users\\Liniker\\Desktop\\')

arquivos = list(scanner)

print(arquivos[0].name)
print(arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].path)
print(arquivos[0].stat())
print(arquivos[0])

# Quando utilizamos a função scandir() nós precisamos fechá-la, assim que abrimos 
# um arquivo

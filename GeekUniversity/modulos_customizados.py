"""
Modulos Customizados

Como modulos Python nada mais são do que arquivos Python, então todos os arquivos
que criamos nesse curso são modulo python pronto para ser utilizados
"""

# from funcoes_com_parametros import soma_impares

# print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Importando todo o módulo
# import funcoes_com_parametros as fcp

# # Estamos acessando e imprimindo uma variável contida no módulo
# print(fcp.lista)

# print(fcp.tupla)

# print(fcp.soma_impares(fcp.lista))

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))
"""
Módulo Collections - Default Dict

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)
print(dicionario['curso'])
print(dicionario.get('curso'))
#print(dicionario['chave_invalida']) # Gera um KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default.
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuido..

OBS: Lambdas são funções sem nome, que podemos ou não receber parâmetros de 
entrada e retornar valores.
https://docs.python.org/3/library/collections.html#collections.defaultdict
"""

# Fazendo o import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)
print(dicionario['outro']) # KeyError no dicionário comum, porém aqui não..

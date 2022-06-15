"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas 
(google, facebook) e terceiros (desenvolvedores)

import json

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)

"""
# import jsonpickle

# class Gato:

#     def __init__(self, nome, raca):
#         self.__nome = nome
#         self.__raca = raca

#     @property
#     def nome(self):
#         return self.__nome

#     @property
#     def raca(self):
#         return self.__raca

# felix = Gato('Felix', 'Vira-Lata')

# print(felix.__dict__)

# ret = jsonpickle.encode(felix)

# print(ret)

# # Integrando o JSON com Pickle

# # pip install jsonpickle

import jsonpickle

# Escrevendo o arquivo JsonPickle
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# Lendo o arquivo JsonPickle

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)

"""
**kwargs

Poderiamos chamar este parâmetro de **xix, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma
esses parâmetros extras em um dicionário.

"""

# # exemplo 

# def cores_favoritas(**kwargs):
#     for pessoa, cor in kwargs.items():
#         print(f'A cor favorita de {pessoa.title()} é {cor}')


# cores_favoritas(a=1, b=2, c=3, marcos="verde", julia="amarelo", fernanda="azul", vanessa="branco")


# # OBS: Os parâmetros *args e **kwargs não são obrigatórios

# cores_favoritas()

# cores_favoritas(geek='navy')

# Exemplo mais complexo

# def cumprimento_especial(**kwargs):
#     if 'geek' in kwargs and kwargs['geek'] == 'Python':
#         return 'Você recebeu um comprimento pythonico geek!'
#     elif 'geek' in kwargs:
#         return f"{kwargs['geek']} Geek!"
#     return "Não tenho certeza quem você é"


# print( cumprimento_especial())
# print( cumprimento_especial(geek="Python"))
# print( cumprimento_especial(geek="Oi"))
# print( cumprimento_especial(geek="especial"))


# Nas nossas funções, podemos ter:

# - Parâmetros obrigatórios;
# - *args;
# - Parâmetro default (não obrigatórios);
# - ** kwargs


# exemplo por ordem

# def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
#     print(f'{nome} tem {idade} anos')
#     print(args)
#     if solteiro:
#         print('Solteiro')
#     else:
#         print('Casado')
#     print(kwargs)
#     print("************PRÓXIMO************")


# minha_funcao(8, "Julia")
# minha_funcao(18, "Felicity", 4, 5, 3, solteiro=True)
# minha_funcao(34, "Felipe", eu='Não', voce="Vai")
# minha_funcao(19, "Carla", 9, 4, 3, java=False, python=True)

# Entenda por quê é importante manter a ordem dos parâmetros na declaração


# Função com a ordem correta dos parâmetros
# def mostra_info(a, b, *args, instrutor="rogerio", **kwargs):
#     return [a, b, args, instrutor, kwargs]

# função com a ordem incorreta de parâmetos
# def mostra_info(a, b, instrutor="Geek", *args, **kwargs):
#     return [a, b, args, instrutor, kwargs]

# """

# a = 1
# b = 2
# args = (3,)
# instrutor = "Geek"
# kwargs = {'sobrenome': 'University', 'cargo': Instrutor}

# """

# print(mostra_info(1, 2, 3, sobrenome="University", cargo="Instrutor"))


# # Desempacotar com kwargs

# def mostra_nomes(**kwargs):
#     return f"{kwargs['nomes']} {kwargs['sobrenome']}"

# nomes = {"nomes": 'Felicity', "sobrenome": 'Jones'}

# print(mostra_nomes(**nomes))


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [2, 3, 5]
tupla = (2, 5, 8)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
# soma_multiplos_numeros(1, 2, 3)


dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS! os nomes da chave em um dicionario devem ser o mesmo dos parâmetros da função

soma_multiplos_numeros(**dicionario, lang="Python")
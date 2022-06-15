"""
Debuggando com PDB

PDB -> Python Debugger
Bug -> Inseto

"""
# # A utilização do print para debugar código, é uma pratica ruim..
# def dividir(a, b):
#     print(f'a={a}, b={b}')
#     try:
#         return int(a) / int(b)
#     except (ValueError, ZeroDivisionError) as err:
#         return f'Ocorreu um problema : {err}'

# print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferente IDEs, como o Pychamr ou VsCode ou utilizando
# o PDB - Python Debugger

# def dividir(a, b):
#     print(f'a={a}, b={b}')
#     try:
#         return int(a) / int(b)
#     except (ValueError, ZeroDivisionError) as err:
#         return f'Ocorreu um problema : {err}'

# print(dividir(4, 0))

# Exemplo com o PDB - Python Debugger

# Para utilizar o Python Debugger, precisamos importar a biblioteca PDB e então utilizar
# a função set_trace()
# comandos básicos do PDB
# l - (listar onde estamos no código)
# n - (próxima linha)
# p - (imprime variável)
# c - (continua a execução - finaliza o debugging)


# import pdb;pdb.set_trace()
# nome = "Liniker"
# sobrenome = "Oliveira"
# nome_completo = nome + " " + sobrenome
# curso = "Programação em Python: Essencial"
# final = nome_completo + " faz o curso " + curso
# print(final)

# Por quê utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Custumamos realizar todos os 
# imports de bibliotecas no inicio do arquivo.


# * A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o
# comando de debug foi incorporado como função built-in (integrada) chamada breakpoint();

nome = "Liniker"
sobrenome = "Oliveira"
breakpoint()
nome_completo = nome + " " + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + " faz o curso " + curso
print(final)

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))


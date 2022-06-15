"""
Documentando funções com Docstrings

OBS: Podemos ter acesso a documentação de uma função em Python utilizando a pro-
priedade especial __doc__

"""

print(help(print))

# Exemplos

def diz_oi():
    """ Uma função simples que retorna uma string oi """
    return 'Oi'

print(diz_oi())
print(help(diz_oi()))
print(diz_oi.__doc__)

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencial' informada
    :param numero: Núemro desejamos gerar o exponencial.
    :param potencia Potência que queremos gerar o exponencial. Por padrão e 2 .
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
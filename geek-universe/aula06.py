import math

def circuferencia(raio):
    #type (float) -> float
    return 2 * math.pi * raio

print(circuferencia(8))
# mypy faz a checagem do tipo no comentário

def cabecalho(texto, alinhamento=True):
    # type (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

# cabecalho1(texto=43, alinhamento='geek')

def cabecalho2(
    texto, # type: str
    alinhamento=True # type: bool
): # type : (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho2(texto='42', alinhamento=False)

nome = 'Liniker Oliveira' # type: str



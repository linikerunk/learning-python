def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n {'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, "#")


print(cabecalho('Geek University'))

print(cabecalho('Geek University', alinhamento=False))

# Em python uma string é considerada True
print(cabecalho('liniker', alinhamento=True))

# Checador de Tipo da linguagem oficial do Python

# # Correto

# texto: str

# # Incorreto

# texto:str
# texto : str

# # Correto
# () -> str:

# # Incorreto
# ()->str
# () ->str

# # Correto
# alinhamento: bool = True

# # Incorreto

# alinhamento:bool=True

# alinhamento: bool= True
# alinhamento : bool =True

import math

def circuferencia(raio: float) -> float:
    return 2 * math.pi * raio

# print(circuferencia.__annotations__)

nome: str = 'Liniker Oliveira'


peso: float = 67.9

ativo: bool = True

print(nome)
print(peso)
print(ativo)
print(__annotations__)


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando.'

p = Pessoa(nome='Liniker', idade=25, peso=90.6)

print(p.__dict__)
# print(p.__annotations__) Não tem annotations

print(p.andar.__annotations__)
print(p.__init__.__annotations__)
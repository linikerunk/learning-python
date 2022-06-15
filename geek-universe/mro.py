"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Metodos), e a ordem de execução
dos métodos (quem será  executados primeiro)

Em Python , a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via, propriedade de classe __mro__
    - Via método mro()
    - Via help
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def nadar(self):
        return f'{self._Animal__nome} está nadando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        return f'{self._Animal__nome} está andando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da Terra!'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return f'Pinguim'


# Testando

tux = Pinguim("Tux")
print(tux.cumprimentar())
print(Pinguim.__mro__)
print(Pinguim.mro())
help(Pinguim)

"""
Pinguim(Aquatico, Terrestre)
Eu sou o Tux do mar!

"""


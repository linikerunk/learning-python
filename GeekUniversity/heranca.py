"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código, mas não só isso, mas tbm extender
nossas classes...

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Perguntar : existe alguma entidade genérica o suficiente que precisamos refator
em uma herança!?

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e mé-
todos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por :
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;
"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessar a super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}'


class Pinguim: # Pinguim não é uma pessoa por causa disso nao pode herdar de pinguim...

    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# print(cliente1.__dict__)
# print(funcionario1.__dict__)

# Sobrescrita de Métodos (Overriding)
# OBS : Sobrescreita de método ocorre quando reescrevemos/reimplementamos um
# método presente na super classe em classes filhas. 

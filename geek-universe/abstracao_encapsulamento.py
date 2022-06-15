"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e
hierarquico utilizando classes.

Encapsular -> capsula.


        classe
-------------------------
/  Atributos e metodos  /  <- Encapsulamento
-------------------------

# Atributos / Métodos privados em Python

Imagine que temos uma classe chamado Pessoa, contendo um atributo privado
chamado __nome e um método privado chamado __falar() esses métodos e atributos
deveriam ser chamado apensa dentro da classe.
Mas em Python acontece um fenômeno chamado Name Magling, que faz uma alteração
na forma de se acessar os elementos privados, conform:

_Classe__elemento

Exemplo - Acessando elemenetos privados fora da classe:

instancia._Pessoa__nome

isntancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escon-
dendo atributos e métodos privados de usuário.

"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de \
{self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O Valor precisa ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("Saldo insuficiente..")
        else:
            print("O valor deve ser positivo")

    def transferir(self, valor, conta_destino):
        # 1 - Removendo o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 # Taxa de transferencia
        
        # 2 - Adicionar o valor na conta destino
        conta_destino.__saldo += valor

# Testando

conta1 = Conta('Haduple', 150.00, 1500.00)

print(conta1.__dict__)

conta1.numero = 42
conta1.titulo = 'troquei pq sou publico'
conta1.saldo = 999999999999999999999
conta1.limite = 111111111111111111111111111111111111

print("\n---------Depois de alterar---------\n")

print(conta1.__dict__)

print(conta1._Conta__titular) # Name Mangling... Errado.
conta1._Conta__titular = 'troquei com o name mangling'

print(conta1.__dict__)

conta1.depositar(400)

print(conta1.__dict__)

conta1.sacar(2500)

print(conta1.__dict__)


conta1 = Conta("Liniker", 300, 3000)
conta1.extrato()

conta2 = Conta("Rafaela", 200, 2500) 
conta2.extrato()

conta1.transferir(300, conta2)

conta1.extrato()
conta2.extrato()

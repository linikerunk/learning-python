"""
POO - Propriedades - Properties

# Em Linguagens de programação como o Java, ao declararmos atributos privados nas
classes. Costumamos a criar métodos públicos para manipulação desses atributos.
Esses métodos sçao conhecidos por getters e settersm onde os getters retornam o
valor do atributos e os setters alterar o valores do mesmo...

"""

# Python fazendo da maneira do Java...
class ContaJava:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = ContaJava.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        ContaJava.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

# Get and Setter...
    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = ContaJava('Felicity', 3000, 2000)
conta2 = ContaJava('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# soma = conta1._Conta__saldo + conta2._Conta__saldo # Não é correto fazer assim
# print(f'A Soma do saldo das contas é {soma}')

soma = conta1.get_saldo() + conta2.get_saldo()  # Maneira correta
print(f'A Soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.set_limite(999999)
print(conta1.__dict__)


# Maneira Pythonica de ser fazer ...

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # Get and Setter pythonico usamos um decorators...

    @property
    def numero(self):
        return self.__numero


    @property
    def titular(self):
        return self.__titular


    @property
    def saldo(self):
        return self.__saldo
    

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
    
    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    #Posso criar uma propriedade para metodos não só para atributos
    @property
    def valor_total(self):
        return self.__saldo + self.__limite

conta1 = Conta('Felicity', 3000, 2000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo # Tipo aqui o saldo é como fosse um atributo mas é uma propriedade
print(f'A Soma do saldo das contas é {soma}')


print(conta1.__dict__)
conta1.limite = 76544
print(conta1.__dict__)

print(conta1.limite)

print(conta2.valor_total)
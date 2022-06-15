"""
POO - Objetos

Objetos -> São instância da classe. Ou seja, após o mapeaento do objeto do mundo
real para sua representação computacional, devemos poder criar quantos objetos
forem neecssário. Podemos pensar nos objetos/instâncias de uma classe como 
variáveis do tipo definidos na classe.

"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False
    
    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz Oi!!')

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')
        print(f'O CPF é {self.__cliente._Cliente__cpf}')
        

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# # Instância / Objetos
# lamp1 = Lampada('Azul', 110, 60)

# lamp1.ligar_desligar()

# print(f'A lampada está ligada? {lamp1.checa_lampada()}')

# cc1 = ContaCorrente(5000, 20000)

# user1 = Usuario('Liniker', 'Oliveira', 'liniker@gmail.com', '159753')

nome = 'Liniker'
sobrenome = 'Oliveira'
email = 'liniker@gmail.com'
senha = '123456'

user = Usuario(nome, sobrenome, email, senha)
print(user.__dict__)
print(repr(user))

cli1 = Cliente('Liniker Oliveira', '427-570-818-02')

cc = ContaCorrente(5000, 10000, cli1)

cc.mostra_cliente()
cc._ContaCorrente__cliente.diz()

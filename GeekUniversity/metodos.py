"""
POO - Métodos

- Metodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema


Em Python, dividimos os métodos, em 2 grupos: Metodos de instância e Métodos 
de Classe.

# O método dunder __init__ é um método especial chamado de construtor e sua função
é construir o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado
de dunder (Double Underline)

OBS: Os métodos dunder em Python são chamados de métodos mágicos

# Métodos são escritos em letras minusculas ...  e separadas por _ se for composto

# Métodos de Classe em Python são conhecidos como Métodos Estáticos em outros
linguagens.

# Métodos de Classe

user = Usuario('Felicity', 'Jones', 'filicity@gmail.com', '123456')

Usuario.conta_usuario() #Forma correta
user.conta_usuario() # Possível, mas incorreta



user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

user._Usuario__gera_usuario() # Acesso, de forma ruim...

"""

#Métodos de Instância

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o vlaor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

# pip install passlib -> biblioteca para criptografia..

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0
    
    @classmethod # O Class method vc recebe a própria class no parametro.
    def conta_usuario(cls):
        print(f'Classe : {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema.')
    
    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod # Método Stático
    def definicao():
        return "UXR344"
    

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado {self.__gera_usuario()}')

    # def __correr__(self, metros): # Não é comum vc criar métodos com Dunder..
    def correr(self, metros):
        print(f"{self.__nome} está correndo à {metros} metros")

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('0')[0]



p1 = Produto('Play 4', 'Video Game', 2300)

print(p1.desconto(50))

# print(Produto.desconto(p1, 50))

user1 = Usuario("Angelina", "Jolie", "angelina@gmail.com", '123456')
user2 = Usuario("Felicity", "Jones", "felicity@gmail.com", '654321')

print(user1.nome_completo())
print(user2.nome_completo())
print(Usuario.nome_completo(user1))
print(f'Senha: {user1._Usuario__senha}') # Acesso errado ...

nome = input('Informe o nome : ')
sobrenome = input('Informe o sobrenome : ')
email = input('Informe o e-mail : ')
senha = input('Informe a senha : ')
confirma_senha = input('Confirme a senha : ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1)

print("Usuário criado com sucesso!")

senha = input('Informe a senha para acesso : ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado.')

print(f"Senha User Criptografada : {user._Usuario__senha}") # Acesso errado

# Método Estático

print(Usuario.contador)
print(Usuario.definicao())

user = Usuario('liniker', 'oliveira', 'liniker@gmail.com', '1598752')

print(user.contador)
print(user.definicao())
"""
POO - Atributos

Atributos - Representam as caracteristicas do objeto. Ou seja, pelo atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de instância; São atributos declarados dentro do método construtor.

#OBS : Método construtor: E um método especial utilizado para a construção do
objeto.

Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos :

public class Lamapada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lamapada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
    public int getVoltagem(){
        return this.voltagem
    }

}


# Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe
é público., ou seja poder ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling.

"""

# Classes com Atributos de instancia publicos
class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    #property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# No lugar do self posso usar um namespace...

class Teste:

    def __init__(cerveja, nome, idade):
        cerveja.nome = nome
        cerveja.idade = idade


# Atributos Publicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha, usuario):
        self.__email = email
        self.__senha = senha
        self.usuario = usuario

    def mostra_senha(self, usuario):
        print(f"Usuário : {self.usuario} tem a senha {self.__senha}")

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python
# não irá impedir se façamos acesso aos atributos sinalizados como privado fora
# da classe

# Exemplo,

user = Acesso('user@gmail.com', '123456', 'userx')

print(user.usuario)
# print(user.__email) # Atribute error..
print(user._Acesso__email) # Temos acesso mas nao deveriamos ter...
#    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Name Mangling.

user.mostra_senha(user.usuario)

# O que significa atributos de instância?

# Significa, que ao criarmos instância/objetos de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso('user1@hotmail.com', '665444222', 'user1')
user2 = Acesso('user2@gmail.com', '147147147', 'user2')

user1.mostra_senha(user1.usuario)
user2.mostra_senha(user2.usuario)


# Atributos de Classes

p1 = Produto('Playstation 4', 'Video Game', 3.000)
p2 = Produto('Xbox One', 'Video Game', 2.200)

# Atributos de classes, são atributos que são declarados diretamente na classe,
# ou seja, fora do construtor. Geralmente já inicializamos um valor, e este valor
# é compartilhado entre todas as instâncias da classe. Ou seja, ao invéz de cada 
# instancia da classe ter seus próprios valores como é o caso dos atributos de
# instância, com os atributos da classe todas as instâncias terão o mesmo valor
# para este atributos.


# Refatorar a classe Produto

class Produto:

    # Atributos de classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Play 4', 'Video Game', 2300)
p2 = Produto('Xbox 360', 'Video Game', 2000)

print(p1.valor)
print(p2.valor)

# OBS : Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributosconhecidos como atributos de classe
# aqui em Python são chamados de atributos estáticos.


# Atributos Dinâmicos -. Um atributo de instância que pode ser criado em tempo de
# execução.

# OBS: O atributo dinâmico será exclusivo de instância que o criou.

p1 = Produto('Play 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercadoria', 5.99)

# Criando um atributo dinâmico em tempo de execução.

p2.peso = '5kg' # Note que na classe Produto não existe o atributo peso

print(f'Produto : {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
# print(f'Produto : {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p1.peso}')

# Deletando Atributos

print(p1.__dict__) # __dict__ Propriedade do nossos objetos
print(p2.__dict__)
print(Produto.__dict__)

# Deletando...

del p2.peso
del p2.valor

print(p1.__dict__) 
print(p2.__dict__)

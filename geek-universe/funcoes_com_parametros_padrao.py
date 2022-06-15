"""
Funções com parâmetro Padrão (default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de funções onde a passagem de parâmetro seja opcional
print("TESTE")
print()

"""


def exponencial(numero, potencial=2):
    return numero ** potencial


print(exponencial(2, 3)) # 2 * 2 * 2 = 8
print(exponencial(3, 3)) # 3 * 3 * 3 = 9

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3, 5))

# OBS

# Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro 
# numero, e será calculado o quadrado deste numero;

# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro numero
# e o segundo parâmetro potencia. Então será calculada esta potência.
# print(exponencial())


# OBS : em função Python, os parâmetros com valores default(padrão) DEVEM sempre
# estar ao final da declaração.


# # ERRO
# def teste(num=2, potencial):
#     return num ** potencial

# print(teste(6))


def soma(num1=0, num2=0):
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(soma())

# Exemplo mais complexo

def mostra_informacao(nome="Geek", instrutor=False):
    if nome == "Geek" and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao("Ozzy"))
print(mostra_informacao(nome="Stephany"))


# por quê utilizar parâmetros com valor default?
#  - Nos permite ser mais flexíveis nas funções; 
#  - Evita erros com parâmetros incorretos;
#  = Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?
# -Quaisquer tipos de dados
    # - String, numeros, float, booleanos, 
    
def diz_oi():
    print('oi')

variavel = diz_oi()
print(variavel)


def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def sub(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, sub))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# variáveis locais

instrutor = 'Geek' # Variável global

def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS : Se tivermos uma variável local com o mesmo nome de uma variável global
# a local terá preferência.

def diz_oi():
    prof = 'Xavion'
    return f'Ola {prof}'

print(diz_oi())
# print(prof) # NameError

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    global total # avisando que queremos utilizar a variavel global.
    total = total + 1 # variavel local está sendo utilizada para processamento sem ter sido chamada
    return total

print(incrementa())
print(incrementa())
print(incrementa())


def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

# print(dentro()) Aqui da erro.

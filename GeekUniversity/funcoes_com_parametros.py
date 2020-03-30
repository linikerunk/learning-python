"""
Funções com parâmetros (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Possuem entrada e saída;
"""

# Refatorando uma função

def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(2))
print(quadrado(9))

ret = quadrado(6)
print(ret)



def cantar_parabens(aniversariante):
    print(f'Parabéns {aniversariante}')

cantar_parabens('Liniker')


# Funções com variaos parâmetros

# Exemplo


def soma(a, b):
    return a + b

def multiplicacao(num1, num2):
    return num1 + num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplicacao(4, 5))
print(multiplicacao(20, 10))

print(outra(4, 5, 'geek'))
print(outra(6, 7, 'Python'))


# OBS : Se a gente informar um número errado de parâmetro ou argumentos, teremos
# um TypeError


# Nomeando parâmetros

def nome_completo(string1, string2):
    return f"Seu nome completo é {string1} {string2}"

print(nome_completo("Angelina", "Jolie"))


# A diferença entre Parâmetros e Argumentos
# Parâmetros são variáveis declaradas na definição de uma função.
# Argumentos são dados passados durante a execução de uma função.


# A ordem dos parâmetros importa!

nome = "Felicity"
sobrenome = "Jones"

print(nome_completo(sobrenome, nome)) # Ordem importa


# Argumentos nomeados (Keyword Arguments)

#Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
#utilizar qualquer ordem.

print(nome_completo(string1="Angelina", string2="Jolie"))
print(nome_completo(string1=nome, string2=sobrenome))


# Erro comum na utilização do return 

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total 


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
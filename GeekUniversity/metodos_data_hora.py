"""
Métodos de Data e Hora


"""

import datetime

#Com now() podemos especificar um timezone (Fuso Hórario)
agora = datetime.datetime.now()# diferença que aqui posso colocar timezone...

print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today() 

print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo à meia-noite

# manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

# print(manutencao)
# print(type(manutencao))
# print(repr(manutencao))


# Encontrar o dia da semana, com o método weekday()


# Os dias da semana do método weekday() começa em 0, sendo essa a segunda - feira
# 0 - Segunda - Feira (Monday)
# 1 - Terça - Feira   (Tuesday)
# 2 - Quarta - Feira (Wednesday)
# 3 - Quinta - Feira (Thursday)
# 4 - Sexta - Feira (Friday)
# 4 - Sábado - Feira (Saturday)
# 4 - Domingo - Feira (Sunday)


# def formata_data(data):
    #     if data.month == 1:
    #         return f'{data.day} de Janeiro de {data.year}'
    #     elif data.month == 2:
    #         return f'{data.day} de Fevereiro de {data.year}'
    #     elif data.month == 3:
    #         return f'{data.day} de Março de {data.year}'
    #     elif data.month == 4:
    #         return f'{data.day} de Abril de {data.year}'
    #     elif data.month == 5:
    #         return f'{data.day} de Maio de {data.year}'
    #     elif data.month == 6:
    #         return f'{data.day} de Julho de {data.year}'
    #     elif data.month == 7:
    #         return f'{data.day} de Junho de {data.year}'
    #     elif data.month == 8:
    #         return f'{data.day} de Agosto de {data.year}'
    #     elif data.month == 9:
    #         return f'{data.day} de Setembro de {data.year}'
    #     elif data.month == 10:
    #         return f'{data.day} de Outubro de {data.year}'
    #     elif data.month == 11:
    #         return f'{data.day} de Novembro de {data.year}'
    #     elif data.month == 12:
    #         return f'{data.day} de Dezembro de {data.year}'

    # Formatando datas/horas com strftime() (String Format Time)
    # dd/mm/yyyy hora:minuto

    # hoje = datetime.datetime.today()

    # print("Função: ", formata_data(hoje))

    # print(hoje)

    # hoje_formatado = hoje.strftime('%d/%m/%Y') #y abreviado com dois, %Y com 4 digitos

    # print(hoje_formatado)

    # hoje_formatado = hoje.strftime('%d/%B/%Y')

    # print(hoje_formatado)

    # hoje_formatado = hoje.strftime('%d de %B de %Y')

    # print(hoje_formatado)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())

aniversario = input('Qual sua data de nascimento? dd/mm/yyy : ')

aniversario = aniversario.split("/")

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print("Você nasceu em uma segunda-feira")
elif aniversario.weekday() == 1:
    print("Você nasceu em uma terça-feira")
elif aniversario.weekday() == 2:
    print("Você nasceu em uma quarta-feira")
elif aniversario.weekday() == 3:
    print("Você nasceu em uma quinta-feira")
elif aniversario.weekday() == 4:
    print("Você nasceu em uma sexta-feira")
elif aniversario.weekday() == 5:
    print("Você nasceu em uma sábado-feira")
elif aniversario.weekday() == 6:
    print("Você nasceu em uma domingo-feira")


# pip install textblob
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.datetime.today()

print(formata_data(hoje))


nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

print(nascimento)


nascimento = input("Qual sua data de nascimento? (dd/mm/yyy) : ")
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)


# Somente Hora

lunch = datetime.time(12, 30, 0) # Hour, Minute, Second
print(lunch)

# Marcando tempo de execução do nosso código com timeit

import timeit, functools

# Loop for 

tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma ** num + 4
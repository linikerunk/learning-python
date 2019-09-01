#Desenvolva um programa para calcular e mostrar o desconto no valor de uma
#compra (fornecido pelo usuário), de acordo com a tabela:
#Valor	Desconto
#-----Menor ou igual a R$ 1000,00     	10%
#-----Maior que R$ 1000,00 e menor ou igual a R$ 5000,00	20%
#-----Maior que R$ 5000,00	30%

# usando thread para ver que você consegue fazer varias coisas com multitarefas..
from threading import Thread
from time import sleep

def call_at_interval(period, callback, args):
    while True:
        sleep(period)
        callback(*args)
        exit(1)

def setInterval(period, callback, *args):
    Thread(target=call_at_interval, args=(period, callback, args)).start()

def imprime(word):
    print("Finalizando", word)




linha = '-' * 110
descricao ="Valor	Desconto  \n \
Menor ou igual a R$ 1000,00  [10%]  \n \
Maior que R$ 1000,00 e menor ou igual a R$ 5000,00 [20%] \n \
Maior que R$ 5000,00 [30%]"
print(linha)
print(descricao.center(20))
print(linha)

# código da regra a partir dessa linha ::

item = float(input("Digite o valor do item que você comprou :"))
if item < 0:
    print('Valor invalido')
    exit(1)

# regra da compra ...
item_result = 0
if item <= 1000:
    item_result += item * (10/100)
    item_result = item - item_result
    print(f'Desconto de 10% valor item: {item:.2f} com desconto {item_result:.2f}')

elif item > 1000 and item <= 5000: 
    item_result += item * (20/100)
    item_result = item - item_result
    print(f'Desconto de 20% valor item: \
{item:.2f} com desconto {item_result:.2f}')

elif item > 5000:
    item_result = item * (30/100)
    item_result = item - item_result
    print(f'Desconto de 30% valor item: \
{item:.2f} com desconto {item_result:.2f}')

setInterval(2, imprime, '...!') # função para chamar o imprimir antes de fechar.
print('Até mais..')






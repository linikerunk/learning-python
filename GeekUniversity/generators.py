"""
Generators

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension... porque eles se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiana', 'Vanessa']

print(any([ nome[0] == 'C' for nome in nomes ]))

"""

# Poderiamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiana', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator ocupa menos recurso em memória..
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)


# Qual a utilizada de getsizeof()? -> retorna a quantidade de bytes em memória do elemento passado como parâmetro.

from sys import getsizeof # saber quantos bytes estão sendo ocupado em memória..
print(getsizeof("Liniker"))

print(getsizeof("Carro que é vermelho é feio"))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(945485754554545))

print(getsizeof(True))


# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando um Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando um Dict Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)}) 

# Com Generators..
gen = getsizeof(x * 10 for x in range(1000))

print("Para fazer a mesma tarefa gastamos em memoria: ")
print(f'List Comprehension: {list_comp}')
print(f'Set Comprehension: {set_comp}')
print(f'Dictionary Comprehension: {dic_comp}')
print(f'Generator Expression: {gen}')

# Eu posso iterar no Generator Expression: Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
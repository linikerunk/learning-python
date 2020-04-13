"""
Teste de Memória com Generators

#Sequencia de fibonacci

1, 1, 2, 3, 5, 8, 13, ...

"""

def fib_lista(maximo):
    nums =[]
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste
for n in fib_lista(100):
    print(n)


# Função usando geradores

def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a # invez de lista estamos usando um gerador...
        contador += 1

for n in fib_gen(100):
    print(n)

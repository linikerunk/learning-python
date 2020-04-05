"""
Len, Abs, Sum, Round

# Len

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

"""

# Só para revisar

print(len("Liniker"))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

# Por de baixo dos panos, quando utilizamos  a função len() o Python faz o seguinte:

# Dunder len
print('Geek University'.__len__())

# Abs

#abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica
# seria o seu valor real sem o sinal.

# Exemplo Abs

print(abs(-5))
print(abs(5))
print(abs(3.1415))
print(abs(-3.1415))

# Sum

# sum() -> Recebe como parâmetro um iterável, podendo receber um vlaor inicial, e 
# retorna a soma total dos elementos, incluindo o valor inicial.

#OBS: O valor inicial default = 0

# Exemplo sum

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], -5))

# podemos usar o sum para :

print(sum([2, 2, 2, 2, 2]))
print(sum((2, 2, 2, 2, 2)))
print(sum({2, 2, 2, 2, 2}))
print(sum({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2}.values()))


# Round 

#round() -> Retorna um número arredondado para n digito de precisao aós a casa decimal
# após a casa decimal. Se a precisão não for informada retorna o inteiro mais próximo da entrada.


# Exemplo Round

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.12455547, 2))
print(round(1.29455547, 2))
print(round(1.29455547))
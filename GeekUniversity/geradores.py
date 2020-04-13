"""
Geradores (Generators) são Iterators (Iteradores);

OBS: O contrário não é verdade nem todo iterator é um genenrator.

Outras informações:
- Generators podem ser criado com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser cirados com Expressoes Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)


-----------------------------------------------------------------------------------
|Funções                                   | Generator Functions                  |
-----------------------------------------------------------------------------------
|Utilizam return                           | Utilizam yield                       |
-----------------------------------------------------------------------------------
|Retorna uma vez                           |Podem utilizar yield multiplas vezes  |
-----------------------------------------------------------------------------------
|Quando executada, retorna um valor        |Quando executada, retorna um generator|
-----------------------------------------------------------------------------------

"""

# funçao Geradora Exemplo Generator Function:

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1
# OBS: Uma Generator Function não é uma Generator. Ela gera um generator, ok ?

gen = conta_ate(5)
print(type(gen))
print(next(gen))
print(next(gen))

gen = list(conta_ate(10))
print(gen)

for num in gen:
    print(num)

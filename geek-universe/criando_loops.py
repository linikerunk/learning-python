"""
Criando sua própria versão do loop

Iterable is an object, which one can iterate over. It generates an Iterator when
passed to iter() method. Iterator is an object, which is used to iterate over 
an iterable object using __next__() method. Iterators have __next__() method,
which returns the next item of the object.

"""

for num in [1, 2 ,3 , 4, 5]:
    print(num)

for letra in 'Linikao':
    print(letra)

# Por baixo dos panos

iter([1, 2, 3, 4, 5, 6])
iter('Linikao')

# ai voce pode dar o next


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Linikao')

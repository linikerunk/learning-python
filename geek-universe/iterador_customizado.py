"""
Escrevendo um iterador customizado


"""

# for n in range(0, 11):
#     print(n)
# Por baixo dos panos

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration
    
cont = Contador(1, 10)

print(cont.menor, cont.maior)

# it = iter(cont)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for n in Contador(1, 10):
    print("Contador : ", n)

for n in range(1, 10):
    print("Range : ", n)

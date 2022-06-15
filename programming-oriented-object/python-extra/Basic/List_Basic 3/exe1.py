#Faça um programa para exibir os números de 1 a 100.


#--------primeira forma----------------
for numeros in range(1, 101):
    print(numeros)
#--------------------------------------
print('***************'*5)
#--------segunda forma-----------------
x = 1
while x != 101:
    print(x)
    x += 1
#--------------------------------------
print('***************'*5)
#--------terceira forma-----------------
lista = []
for items in range(1, 101):
    lista.append(items) 

for numeros in lista:
    print(numeros)

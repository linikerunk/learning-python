#faça um programa que compare se o numero digitado pelo usuario existe na lista estática..

lista = []

lista2 = [1, 2, 3, 4, 5]

lista3 = []

n = int(input("Digite o tamanho da sua lista : "))

for i in range(0, n):
    elemento = int(input("Digite um elemento para sua lista:"))
    lista.append(elemento)

for i in range(len(lista)):
    if lista2[i] == lista[i]:
        lista3.append(lista[i])

print("Os elementos existentes na lista são :", lista3)
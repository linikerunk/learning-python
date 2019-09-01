#Faça um programa que receba um 
#número e diga se este número está no intervalo entre 100 e 200.

linha = '-' * 110
titulo ="Veja se o Número está entre 100 e 200."
print(linha)
print(titulo.center(50))
print(linha)
# Aqui é o código, ali em cima era apenas para fazer um menu...

continuar = 'SIM'
while continuar is not 'NAO':   
    numero = float(input(" Digite um número : "))

    if numero >= 100 and numero <= 200:
        print(f'O número {numero:.2f} está no intervalo de [100] --à-- [200]')
    else: 
        print(f'O número {numero:.2f}  NÂO está no intervalo de [100] --à-- [200]')
    continuar = str(input('Deseja verificar outronúmero : [sim] ou [nao] :'))
    continuar = continuar.upper()
    if continuar == 'NAO':
        exit(1)



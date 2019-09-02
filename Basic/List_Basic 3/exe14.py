#Escreva um programa que leia números inteiros do teclado.
#O programa deve ler os números até que o usuário digite 0 (zero). 
#No final da execução, exiba a quantidade de números digitados, assim como a soma
#e a média aritmética.

numeros_dig = ""
qtn_numeros = 0
soma = 0
while numeros_dig != 0:

    def sair():
        if numeros_dig == 0:
            print('*'*50)
            media = (soma/qtn_numeros-1)
            print(f' A Média é : {media}')
            print('Saindo do programa...')
            exit(1)


    print("Digite um número Inteiro [ou 0 para Sair] :")
    numeros_dig = int(input())
    soma += numeros_dig
    if numeros_dig == 0:
        sair()
    qtn_numeros += 1
    print(f' A quantidade de números digitados foram : {int(qtn_numeros)}')
    print(f' A Soma dos números digitados é : {int(soma)}')






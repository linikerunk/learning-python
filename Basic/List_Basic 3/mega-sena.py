from random import sample
from time import sleep

def megasena():
    jogos=list()
    print("*"*5," MegaSena ","*"*5)
    n=int(input('Quantos jogos?: '))
    for c in range(n):
        a=sorted(sample(range(1, 61), 6))
        jogos.append(a[:])
        print(f'Jogo {c+1}: {a}')
        sleep(0.5)

def lotofacil():
    jogos=list()
    print("*"*5," Lotofácil ","*"*5)
    n=int(input('Quantos jogos?: '))
    for c in range(n):
        a=sorted(sample(range(1, 25), 15))
        jogos.append(a[:])
        print(f'Jogo {c+1}: {a}')
        sleep(0.5)

def sair():
    print("Programa Finalizado")
    exit()

if __name__ == "__main__":
    while True:
        opcao = int(input("Digite [1 - MegaSena] ou [2 - Lotofácil] ou [3 - Sair] : "))
        if opcao == 1:
            megasena()
        elif opcao == 2:
            lotofacil()
        elif opcao == 3:
            sair() 
        else:
            print("Digito inválido digite novamente..")
            opcao = int(input("Digite [1 - MegaSena] ou [2 - Lotofácil] ou [3 - Sair]"))

from random import sample
from time import sleep
from itertools import permutations
from itertools import combinations


def gera_jogos():
    jogos = list()
    contador = 0
    pares = []
    impares = []

    r = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 15)
    for x, i in enumerate(r):
        print("Jogo Nº: ", x, "[", i, "]")
        if i[0] > 4 :
            pass
        elif i[0] <= 4:     
            if sum(i) % 2 == 0:
        
        
        contador += 1
    print("Jogos Gerados : ", contador)



def lotofacil():
    jogos = list()
    gera_jogos()

def sair():
    print("Saindo do sistema...")
    sleep(0.5)
    print("1.")
    sleep(0.2)
    print("2..")
    sleep(0.2)
    print("3...")
    sleep(0.2)
    print("Programa Finalizado")
    exit()


if __name__ == "__main__":
    while True:
        opcao = int(input("[1 - Gerar Lotofácil] ou [0 - Sair] : "))
        if opcao == 1:
            lotofacil()
        elif opcao == 0:
            sair()
        else:
            print("Digito inválido digite novamente..")

    '''
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p6 = 0
    p7 = 0
    p8 = 0
    p9 = 0
    p10 = 0
    p11 = 0
    p12 = 0
    p13 = 0
    p14 = 0
    p15 = 0
    print("To aqui")
    for p1 in range(p1, 11):
        print("Começando p1:")
        print(p1)
        p1 += 1
        for p2 in range(p1, 12):
            print("Começando p2:")
            print(p2)
            p2 += 1
            for p3 in range(p2, 12):
                print("Começando p3:")
                print(p3)
                p3 += 1
                for p4 in range(p3, 12):
                    print("Começando p4:")
                    print(p4)
                    p4 += 1
                    for p5 in range(p4, 12):
                        print("Começando p5:")
                        print(p5)
                        p5 += 1
                        for p6 in range(p5, 12):
                            print("Começando p6:")
                            print(p6)
                            p6 += 1
                            for p7 in range(p6, 12):
                                print("Começando p7:")
                                print(p7)
                                p7 += 1
                                for p8 in range(p7, 12):
                                    print("Começando p8:")
                                    print(p8)
                                    p8 += 1
                                    for p9 in range(p8, 12):
                                        print("Começando p9:")
                                        print(p9)
                                        p9 += 1
                                        for p10 in range(p9, 12):
                                            print("Começando p10:")
                                            print(p10)
                                            p10 += 1
                                            for p11 in range(p10, 12):
                                                print("Começando p11:")
                                                print(p11)
                                                p11 += 1
                                                for p12 in range(p11, 12):
                                                    print("Começando p12:")
                                                    print(p12)
                                                    p12 += 1
                                                    for p13 in range(p12, 12):
                                                        print("Começando p13:")
                                                        print(p13)
                                                        p13 += 1
                                                        for p14 in range(p13, 12):
                                                            print("Começando p14:")
                                                            print(p14)
                                                            p14 += 1
                                                            for p15 in range(p14, 12):
                                                                print("Começando p15:")
                                                                print(p15)
                                                                p15 += 1
                                                                contador += 1
                                                                print(
                                                                    "Número: ", contador, "Jogo:", jogos)
                                                                    '''

def get_numeros():
    jogos = 15
    while jogos == 15:
        jogos = input("Digite uma lista: [1,2,3,4,5,...] : ").split(",")
        jogos = list(jogos)
        if len(jogos) > 15 or len(jogos) < 15:
            print("Digite 15 números")
            get_numeros()
    return verifica_par_impar(jogos)
    


def verifica_par_impar(jogos):
    new_jogos = [x for x in jogos if x.isdigit()]
    pares = []
    impares = []
    for i in range(len(new_jogos)):
        if (int(new_jogos[i]) % 2) == 0:
            pares.append(new_jogos[i])
        elif (int(new_jogos[i]) % 2) == 1:
            impares.append(new_jogos[i])
    count_pares = len(pares)
    count_impares = len(impares)
    print(f"Você tem {count_pares} Pares, sendo eles : {pares}. \n")
    print(f"Você tem {count_impares} Impares, sendo eles : {impares}. \n")

    
def main():
    get_numeros()

    

if __name__ == '__main__':
    main()

'''
for i in range(len(jogos)):
    if (jogos[i] % 2) == 0:
        print(jogos[i], "Par")
        pares.append(jogos[i])

    elif (jogos[i] % 2) == 1:
        print(jogos[i], "Impar")
        impares.append(jogos[i])

print("Pares : ", pares)
print("Impares : ", impares)
'''

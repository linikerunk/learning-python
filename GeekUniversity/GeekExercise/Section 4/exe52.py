"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que
cada deu a reralização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio,
e imprima quanto cada um ganharia de prêmio com base no valor investido.
"""
while True:
    valor_aposta = input("Digite o valor que será apostado : ")
    qnt_pessoa = input("Quantos apostadores vão participar : ")

    try:
        valor_aposta = float(valor_aposta)
        qnt_pessoa = int(qnt_pessoa)
    except:
        print("Digito inválido, digite novamente.")

    def gera_jogadores(qnt_pessoa, *args):
        print(apostas)
        print(qnt_pessoa)        
        for indice in range(1, int(qnt_pessoa) + 1):
            pessoa = input(f"Informe o valor da aposta do jogador {indice} : ")
            pessoa = float(pessoa)
            apostas.append(pessoa)
        return apostas

    apostas = []
    gera_jogadores(qnt_pessoa, *apostas)


    if sum(apostas) != float(valor_aposta):
        print("Divisao das apostas não está certa ..  ")
    else:
        for indice, percentual in enumerate(apostas):
            print(f"Jogador {indice}  irá ganhar {apostas[percentual]} % do valor {sum(apostas)}")





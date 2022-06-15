import time


def sair():
    print("Finalizando Sistema...")
    print('1')
    time.sleep(0.5)
    print('2')
    time.sleep(0.5)
    print('3')
    time.sleep(0.5)
    print("Sistema Finalizado")
    exit()


def inserir(lista):
    opcao = '2'
    elemento = input("Digite o elemento que gostaria de inserir : ")
    while opcao == '2':
        if elemento.isdigit():
            lista.append(elemento)
            print(lista)
            opcao = input(
                "Deseja adicionar um outro elemento? : [1 - SIM] [Qualquer Número - NÃO]: ")
            if opcao == '1':
                inserir(lista)
            else:
                print(lista)
                return main()
        else:
            elemento = input("O elemento deve ser um número: ")


def remover(lista):
    opcao = '2'
    remover_item = input("Qual elemento deseja remover : ")
    while opcao == '2':
        if remover_item.isdigit():
            if int(remover_item) in lista:
                print(remover_item)
                print(lista)
                lista.remove(int(remover_item))
                print(lista)
                print(f"O elemento : {remover_item} foi removido da lista.")
                opcao = input(
                    "Deseja remover outro elemento ? : [1 - SIM] [Qualquer número- NÃO] :")
                if opcao == '1':
                    remover(lista)
                else:
                    main()
            else:
                print("Elemento não existe na lista...")
                main()
        else:
            remover_item = input(
                "Não podemos remover um elemento que não é número, digite um número: ")


def imprimir(lista):
    for x, y in enumerate(lista):
        print(f'Indice : {x} valor : {y}')
    print(f"Sua lista Inteira é : {lista}")


def ordenarc():
    print("***ORDENAR CRESCENTE***")
    pass


def ordenard():
    print("***ORDENAR DECRECENTE***")
    pass


def embaralhar():
    print("***EMBARALHAR***")
    pass


def main():
    lista = list()
    opcao = '0'
    while opcao == '0':
        opcao = input(
            " \n  \
           1 - Inserir um elemento na linha :  \n \
            2 - Remover um elemento da linha : \n \
            3 - Imprimir todos elementos da linha: \n \
            4 - ordenar a linha (ordem crescente): \n \
            5 - ordenar a linha (ordem decrecente): \n \
            6 - Embaralhar a linha : \n \
            sair - Sair do Sistema... \n \
            Opção : ")

        if opcao == '1':
            lista = inserir(lista)
            return lista
        elif opcao == '2':
            lista = remover(lista)
            return lista
        elif opcao == '3':
            lista = imprimir(lista)
            return lista
        elif opcao == '4':
            ordenarc()
        elif opcao == '5':
            ordenard()
        elif opcao == '6':
            embaralhar()
        elif opcao == 'sair':
            sair()
        elif opcao == None:
            print("Opção inválida, Digite novamente...")
            main()
        else:
            print("Opção inválida, Digite novamente...")
            main()


if __name__ == '__main__':
    main()

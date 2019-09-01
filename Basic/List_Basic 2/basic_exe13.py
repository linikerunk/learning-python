#Faça um programa que determine se um ano é bissexto.
#Observação: São bissextos todos os anos divisíveis por 4,
#excluindo os que sejam divisíveis por 100, porém,
#não os que sejam divisíveis por 400.


def main():
    while True:
        sistem = str(input('Digite [iniciar] para iniciar o sistema \
\nou [desligar] para sair do sistema : '))
        sistem = sistem.upper()
        if sistem == 'DESLIGAR':
            print('Saindo do Sistema...')
            exit(1)

        elif sistem == 'INICIAR':
            ano = int(input('Digite o ano para saber se é bissexto : '))
            print('*****************RESULTADO******************')
            if ano % 400 == 0:
                print(f' {ano} é um ano bissexto.')

            elif ano % 4 == 0 and ano % 100 != 0:
                print(f' {ano} é um ano bissexto')
            
            else:
                print('Não é um ano bissexto..')
            print('********************************************')


if __name__ == '__main__':
    main()
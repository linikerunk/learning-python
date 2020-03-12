"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma
mensagem de erro se a opção for inválida: 
"""

def add(number_one, number_two):
    result = number_one + number_two
    return result

def diff(number_one, number_two):
    result = abs(number_one) - number_two
    return result

def mult(number_one, number_two):
    result = number_one * number_two
    return result

def div(number_one, number_two):
    if number_two == 0:
        print("Não pode ser dividido por 0")
        return 0
    else:
        result = number_one / number_two
        return result

if __name__ == "__main__":
    while True:
        print("Escolha a opção : \n \
1 - Soma de 2 números : \n \
2- Diferença entre 2 números (maior pelo menor) : \n \
3 - Produto entre 2 números : \n \
4 - Divisão entre 2 números (o denominador não pode ser zero) : \t ")
        option = input()
        number_one = input("Digite o primeiro número : ") 
        number_two = input("Digite o segundo número : ")
        try:
            number_one, number_two = float(number_one), float(number_two)
        except:
            print("Digito inválido.")
        finally:
            if option == '1':
                print(f"\n A soma dos digitos {number_one}, {number_two} é igual a : {add(number_one, number_two)}")
            elif option == '2':
                print(f"\n A diferença dos digitos {number_one}, {number_two} é igual a : {diff(number_one, number_two)}")
            elif option == '3':
                print(f"\n A multiplicação dos digitos {number_one}, {number_two} é igual a : {mult(number_one, number_two)}")
            elif option == '4':
                print(f"\n A div dos digitos {number_one}, {number_two} é igual a : {div(number_one, number_two)}")
            else:
                print("O digito foi inválido.")
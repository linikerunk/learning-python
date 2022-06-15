"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das 
seguintes categorias:
        |  Categoria  |         Idade         |
        |  Infantil A |     5  a  7           |
        |  Infantil B |     8  a 10           |
        |  Juvenil A  |     11 a 13           |
        |  Juvenil B  |     14 a 17           |
        |    Sênior   |   maiores de 18 anos  |

"""
while True:
    swimmer = input("Digite a idade do nadador : ")
    try:
        swimmer = int(swimmer)
    except:
        print("Digito inválido.")
    finally:
        if swimmer >= 5 and swimmer <= 7:
            print("Nadador categoria [ Infantil A ].")
        elif swimmer >= 8 and swimmer <= 10:
            print("Nadador categoria [ Infantil B ].")
        elif swimmer >= 11 and swimmer <= 13:
            print("Nadador categoria [ Juvenil A ].")
        elif swimmer >= 14 and swimmer <= 18:
            print("Nadador categoria [ Juvenil B ].")
        else:
            print("Nadador categoria [ Sênior ].")
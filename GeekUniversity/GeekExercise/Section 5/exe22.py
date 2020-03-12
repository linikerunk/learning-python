"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
aposentar. As condições para aposentadoria são:
    * Ter pelo menos 65 anos;
    * Ou ter trabalhado pelo menos 30 anos;
    * Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""

while True:
    age = input("Digite a idade da pessoa : ")
    time_service = input("Digite o tempo de trabalho da pessoa  em anos : ")
    try:
        age, time_service = int(age), int(time_service)
    except:
        print("Digito inválido.")
    finally:
        if age >= 60 and time_service >= 25:
            print("Pessoa pode se aposentar.")
        elif age >= 65:
             print("Pessoa pode se aposentar.")
        elif time_service >= 30:
            print("Pessoa pode se aposentar.")
        else:
            print("Pessoa NÃO pode se aposentar.")

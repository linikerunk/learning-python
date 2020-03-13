"""
Escrever um programa que leia o código do produto escolhido do cardápio de uma
lanchonete e a quantidade. O programa deve calcular o valor a ser pago por
aquele lanche. Considere que a cada execução somente será calculado um pedido.
O cardápio da lanchonete segue o padrão abaixo.
            __________________________________________
            |    Especificação    | Código  | Preço  |
            |   Cachorro Quente   |   100   |  1,20  |
            |    Bauru Simples    |   101   |  1,30  |
            |    Bauru com Ovo    |   102   |  1,50  |
            |     Hamburguer      |   103   |  1,20  |
            |   Cheeseburguer     |   104   |  1,70  |
            |       Suco          |   105   |  2,20  |
            |     Refrigerante    |   106   |  1,00  |
            |________________________________________|
"""
total_value, value = 0, 0
while True:
    code = input(" Escolha sua opção via código.\n \
    __________________________________________ \n \
    |    Especificação    | Código  | Preço  | \n \
    |   Cachorro Quente   |   100   |  1,20  | \n \
    |    Bauru Simples    |   101   |  1,30  | \n \
    |    Bauru com Ovo    |   102   |  1,50  | \n \
    |     Hamburguer      |   103   |  1,20  | \n \
    |   Cheeseburguer     |   104   |  1,70  | \n \
    |       Suco          |   105   |  2,20  | \n \
    |     Refrigerante    |   106   |  1,00  | \n \
    |________________________________________| \n \
Opção : ")
    amount = input("Digite a quantidade do item selecionado : ")

    try:
        code, amount = int(code), int(amount)
    except:
        print("Digito inválido.")
    finally:
        tables = {
            100 : ("Cachorro Quente", 1.20), 
            101 : ("Bauru Simples", 1.30), 
            102 : ("Bauru com Ovo", 1.50),
            103 : ("Hamburguer", 1.20),
            104 : ("Cheeseburguer", 1.70),
            105 : ("Suco", 2.20),
            106 : ("Refrigerante", 1.00),
                }
        if code in tables:
            value = (tables[code][1] * amount)
        
        total_value += value

        cont = input("Deseja pedir algo à mais : [SIM] [NAO] : ")

        if cont.upper() == "SIM":
            print(f"Conta até o exato momento : R$ {round(total_value, 2)}")
            pass
        else:
            print(f" Sua conta ficou : R$ {round(total_value, 2)},\
 Obrigado e volte sempre ") 
            
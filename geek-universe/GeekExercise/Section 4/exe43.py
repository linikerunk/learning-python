"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido,
mostre:
    * O total a pagar com desconto de 10%;
    * O valor de cada parcela, no parcelamento de 3 x sem juros;
    * A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com
    desconto. )
    * A comissão do vendedor, no caso da venda ser parcelada
    (5% sobre o valor total)
"""
def metodo_pagamento(pagamento, valor_total):
    print("Pagamento...")
    if pagamento == "A vista":

        valor_total = round((valor_total - (valor_total * 0.10)), 2)
        comissao = round((valor_total * 0.05), 2)
        imprimir_vista(valor_total, comissao)

    elif pagamento =="Parcelado":
        valor_total = round((valor_total / 3), 2)
        comissao = round((valor_total * 0.05), 2)
        imprimir_parcelado(valor_total, comissao)

def imprimir_vista(valor_total, comissao):
    print(f'Valor a se pagar : {valor_total} R$, comissão sobre venda : {comissao} R$')

def imprimir_parcelado(valor_total, comissao):
    print("Imprimindo..")
    print(f'Valor a se pagar : 3x (parcelas) de {valor_total} R$, comissão sobre venda : {comissao} R$')

if __name__ == "__main__":
    valor_total = input("Digite o valor total do item : ")
    pagamento = input("Digite a forma de pagamento [A vista] ou [Parcelado] : ")

    try:
        valor_total = float(valor_total)
        pagamento = str(pagamento)
        pagamento = pagamento.capitalize()
    except:
        print("Digito inválido.")
    metodo_pagamento(pagamento, valor_total)

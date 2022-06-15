"""
Faça um programa para ler as dimensões de um terreno (comprimento [c] x largura [l]),
bem como o preço do metro de tela [p]. Imprima o custo para cercar este mesmo terreno com tela.
"""

while True:
    comprimento = input("Digite o [Comprimento] do terreno : ") 
    largura = input("Digite o [Largura] do terreno : ")
    preco_tela = input("Digite o [Preco Tela] : ")
    try:
        comprimento = round(float(comprimento), 2)
        largura = round(float(largura), 2)
        preco_tela = round(float(preco_tela), 2)
    except:
        print("Digito inválido : ")
    
    custo_total = (comprimento * largura) * preco_tela
    print(f"Para cerca o terreno de comprimento : {comprimento}, largura : {largura}, com o preco da tela : {preco_tela} \
\n Você irá gastar : R$ {round(custo_total, 2)}")
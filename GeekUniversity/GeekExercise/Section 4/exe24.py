"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A fórmula
de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e A área em acres.
"""

while True:
    metros = input("Digite o valor em metros quadrado : ")
    try: 
        metros = float(metros)
        acres = ( metros * 0.000247 )
        print(f"{metros} Metros convertido em Acres é igual a : {round(acres, 4)}")
    except:
        print("Digite um valor válido..")
"""
Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A fórmula de conversão
é igual a M = A * 4048.58, sendo M a área em metros quadrados e A a área em acres..
"""

while True:
    acres = input("Digite o valor em Acres : ")
    try: 
        acres = float(acres)
        metros = ( acres * 4048.58 )
        print(f"{acres} Acres convertido em Metros é igual a : {round(metros, 2)}")
    except:
        print("Digite um valor válido..")
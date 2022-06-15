"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo,
calcule e escreva o preço novo, e escreva uma mensagem em função do proço novo
(de acordo com a segunda tabela).
__________________________________________________
|PREÇO ANTIGO            | PERCENTUAL DE AUMENTO |
|------------------------------------------------|
|até R$ 50               |          5%           |
|entre R$ 50 e R$ 100    |         10%           |
|acima de R$ 100         |         15%           |
└------------------------------------------------╛

________________________________________________________
|PREÇO NOVO                        | MENSAGEM          |
|------------------------------------------------------|
|até R$ 80                         |     Barato        |
|entre R$ 80 e R$ 120 (inclusive)  |     Normal        |
|entre R$ 120 e R$ 200 (inclusive) |     Caro          |
|acima de R$ 200                   |     Muito Caro    |
└------------------------------------------------------╛
"""
old_price = input("Digite o preço antigo : ")
try:
    old_price = float(old_price)
except:
    print("Digito inválido.")

if old_price < 50 and old_price > 0:
    new_price = (old_price * 0.05) + old_price
elif old_price >= 50 and old_price <= 100:
    new_price = (old_price * 0.10) + old_price
elif old_price > 100:
    new_price = (old_price * 0.10) + old_price
else:
    print("Preço inválido")

if new_price <= 80 and new_price > 0:
    print(f"Novo preço : {new_price}")
    print("Barato")
elif new_price > 80 and new_price < 120:
    print(f"Novo preço : {new_price}")
    print("Normal")
elif new_price >= 120 and new_price < 200:
    print(f"Novo preço : {new_price}")
    print("Caro")
elif new_price > 200:
    print(f"Novo preço : {new_price}")
    print("Muito Caro")
else:
    print("Calculo de reajuste inválido")
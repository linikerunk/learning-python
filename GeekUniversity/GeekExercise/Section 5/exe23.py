"""
Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se
for divisível por 400 ou se for divisível por 4 e não for divisível por 100 
Por exemplo: 1988, 1992, 1996
"""

while True:
    year = input("Digite um ano para saber se é bissexto ou não : ")
    try:
        year = int(year)
    except:
        print("Digito inválido.")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Ano {year} é bissexto.")
    else:
        print(f"Ano {year} NÃO é bissexto.") 
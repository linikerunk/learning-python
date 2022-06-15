"""
Leia quatro notas, calcule a média aritmética e imprima o resultado.
"""
notas = []
cont = int(input("Digite quantas notas : "))
num = 0
for num, indice in enumerate(range(1, (cont+1))):
    print("Digite o ", indice, " Número : ")
    num = input()
    try:
        num = float(num)
        print("estou tentando")
    except:
        print(" Valor Inválido.")
    notas.append(num)
media = (sum(notas) / len(notas)) 
print(f"A média Aritmédia dos números {notas[0]}, {notas[1]}, {notas[2]} é igual a {round(media, 2)}")

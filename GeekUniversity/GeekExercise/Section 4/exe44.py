"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. calcule e mostre quantos degraus o usuário deverá subir para
atingir seu objetivo.
"""

altura_grau = input("Digite a altura do degrau em metros : ")
altura_desejada = input("Digite a altura que deseja alcançar : ")

try:
    altura_grau = float(altura_grau)
    altura_desejada = float(altura_desejada)
except:
    print("Digito inválido..")

degraus = altura_desejada / altura_grau  

print(f"{round(degraus, 1)} Degraus!")
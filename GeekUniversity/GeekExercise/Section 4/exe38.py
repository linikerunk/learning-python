"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
sabendo que ele recebeu um aumento de 25%;
"""

while True:
    try:
        salario = input("Digite o salário do funcionario : ")
        salario = float(salario)
        novo_salario = salario + (salario * 0.25)
        print("Salário depois de 25% de aumento.")
        print(f"R$ : {novo_salario}")
    except:
        print("Valor inválido..")
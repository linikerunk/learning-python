"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,
sabendo-se que esse funcinário tem uma gratificação de 5% sobre o salario-base.
Além disso, ele paga 7% de imposto sobre o salário-base.
"""

salario_base = input("Digite o sálario-base do funcionário : ");
try:
    salario_base = float(salario_base)
    gratificacao = salario_base * 0.05
    imposto_salario_base = salario_base * 0.07
    print(f"O sálario do funcionário é : {salario_base + gratificacao - imposto_salario_base}")
except:
    print("Digito inválido..")
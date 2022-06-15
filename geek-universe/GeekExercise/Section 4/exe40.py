"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que 
solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida
que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""

SALARIO_POR_DIA = 30

dias_trabalhados = input("Digite o número de dias trabalhados : ")
try:
    dias_trabalhados = int(dias_trabalhados)
    imposto_renda = (SALARIO_POR_DIA * dias_trabalhados) * 0.08
    print(f' Sálario com desconto de 8% \
do imposto de renda : {(SALARIO_POR_DIA * dias_trabalhados) - imposto_renda}')
except:
    print("Dígito Inválido...")
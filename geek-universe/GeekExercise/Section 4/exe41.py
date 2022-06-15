"""
Faça um programa que leia o valor da hora de trabalho (em reais) e número de 
horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando
10% sobre o valor calculado.
"""

valor_hora_trabalho = input("Valor da hora trabalhada : ")
horas_trabalhadas = input("Quantas horas trabalhadas : ")
try:
    valor_hora_trabalho = float(valor_hora_trabalho)
    horas_trabalhadas = int(horas_trabalhadas)
    acrescimo_salarial = (valor_hora_trabalho * horas_trabalhadas) * 0.10
    print(f"Valor a ser pago ao funcionário : {(valor_hora_trabalho * horas_trabalhadas) + acrescimo_salarial }")
except:
    print("Digito inválido.")
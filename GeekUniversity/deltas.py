"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:55:33.99334
data_final = dd/mm/yyyy   13:34:23.63554

delta = data_final - data_inicial
"""

import datetime

data_hoje = datetime.datetime.now()

aniversario = input("Digite seu aniversário dd/mm/yyyy : ")
aniversario = aniversario.split("/")

aniversario = datetime.datetime(int(data_hoje.year), int(aniversario[1]), int(aniversario[0]))
print(aniversario)
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))

print(tempo_para_evento)


print("\n Regra Boleto")

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)

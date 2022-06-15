"""
Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
"""
import datetime



ano_atual = datetime.datetime.now().strftime('%m-%d-%Y')
ano_atual = str(ano_atual)
ano_atual = datetime.datetime.strptime(ano_atual, '%m-%d-%Y')
print(ano_atual)

ano_nascimento = input("Digite o ano mês e dia de nascimento 00-00-0000 : ")
nascimento = datetime.datetime.strptime(ano_nascimento, "%m-%d-%Y")

print(type(ano_atual))
print(type(nascimento))
diff = ano_atual - nascimento

print("Sua idade é:", int((diff.days / 30) / 12))


print("Ano atual :", ano_atual, "Digitado : ", ano_nascimento)
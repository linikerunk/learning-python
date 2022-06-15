#Escreva um programa que pergunte o valor inicial de uma dívida e o juros mensal.
#Pergunte também o valor mensal que será pago. Imprima o número de meses para
#que a dívida seja paga, o total pago e o total de juros pago .

initial_value = float(input("Initial debt value : "))# 100
rate = float(input('Input the monthly tax rate in % [without %] : ')) # 1
payment = float(input('Monthly payment : ')) # 25

months_debt = initial_value / payment
interest = initial_value * (rate/100) * months_debt
final_value = initial_value + interest

print(f"You'll pay this debt during {int(months_debt)} month(s).")
print(f"You'll pay an interest of U$ {interest:.2f} for the debt of {initial_value}")
print(f"After {int(months_debt)} month(s), \
you'll have paid U$ {final_value:.2f}")
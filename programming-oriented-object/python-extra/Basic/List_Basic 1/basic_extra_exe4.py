#Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem do aumento.
#Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o sálario inicial : "))
taxa = float(input("Digite a taxa de aumento do sálario : "))

aumento = salario * (taxa/100)

print(f"O sálario {salario} atual com aumento de  \
{taxa} % é : {salario + aumento:.2f}")
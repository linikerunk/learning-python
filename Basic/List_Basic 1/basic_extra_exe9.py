# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule
# quantos dias de vida um fumante perderá. Exiba o total em dias.


qnt_cigarro_dia = int(input("Quantos cigarros a pessoa fuma por dia : "))
qnt_anos = int(input("Quantos anos você já fumou : "))

totalCigarros = (qnt_anos * 365)* qnt_cigarro_dia
vida_perdida = (totalCigarros * 10)/24

print("Dias perdidos de vida : %d" %vida_perdida)



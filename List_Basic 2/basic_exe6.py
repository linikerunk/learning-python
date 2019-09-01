# Escreva um programa para ler as três notas obtidas por um aluno durante o semestre.
# Calcular a sua média (aritmética) e informar a sua menção Aprovado
# (media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 e 6.9). 

soma = 0
for nota in range(3):
    nota = float(input(f'Digite a {nota + 1} Nota : '))
    while nota > 10 or nota < 0: 
        if nota > 10 or nota < 0:
            nota = float(input(f' Nota invalida, Máximo -> [10] Minimo -> [0]:'))
    soma += nota

media = (soma / 3)
print(f"Sua media é {media:.2f}")
if media >= 7: print("Parabéns você está Aprovado.")
elif media <= 5: print("Infelizmente você está Reprovado.")
elif media > 5.1 and media < 6.9:
    print(f'Você está de recuperação, pois sua média é : {media:.2f}')


    
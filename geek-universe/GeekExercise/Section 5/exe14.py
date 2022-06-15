"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente,
a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas anteriormente
obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3, Exame Final : 5. De acordo com o resultado, mostre na
tela se o aluno está reprovado (média entre 0 a 2,9 ) de recuperação (3 entre 4,9) ou se foi aprovado. Faça todas as veri-
ficações necessárias.
"""

while True:
    grade = input("Digite a nota do exame final : ")
    work_school = input("Digite a nota do trabalho : ")
    semiannual_evaluation = input("Digite a nota do exame semestral : ")
    try:
        grade = float(grade); work_school = float(work_school); semiannual_evaluation = float(semiannual_evaluation)
    except:
        print("Digito inválido.")
    finally:
        if grade < 0 or grade > 10:
            print("Nota do exame final deve estar entre 0 e 10.")
        elif work_school < 0 or work_school > 10:
            print("Nota do trabalho deve estar entre 0 e 10.")
        elif semiannual_evaluation < 0 or semiannual_evaluation > 10:
            print("Nota do exame semestral deve estar entre 0 e 10.")
        else:
            weighted_average = ((grade * 5 ) + (work_school * 2) + (semiannual_evaluation * 3)) / 10
            if weighted_average > 0 and weighted_average <= 2.9:
                print(f'Média {weighted_average}, aluno está reprovado.')
            elif weighted_average >= 3 and weighted_average <= 4.9:
                print(f'Média {weighted_average}, aluno está recuperação.')
            else:
                print(f'Média {weighted_average}, aluno está Aprovado.')
            print("Deu certo")
        
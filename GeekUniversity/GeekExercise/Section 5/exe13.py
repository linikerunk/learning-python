"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A prime-
ira e a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a
média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para apro-
vação deve ser igual ou superior a 60 pontos.
"""

grades = []

while True:
    grade = input("Digite a nota : ")
    try:
        grade = float(grade)
    except:
        print("Digito inválido.")
    finally:
        if grade < 0 or grade > 10:
            print("Nota deve estar entre 0 e 10.")
        # else:
        #     grades.append(grade)
        #     weighted_average = 0; sum_grades = 0
        #     if len(grades) == 3:
        #         for index, value in enumerate(grades):
        #             print(grades[0], grades[1], grades[2])
        #             if index < 2:
        #                 sum_grades += (value / 0.25) * 1
        #                 print("troasdjsad")
        #             elif index == 2:
        #                 sum_grades += (value / 0.50) * 1
        #                 print(sum_grades)    
        #                 weighted_average = sum_grades / len(grades)
        #                 print(f"Média ponderada é igual a : {weighted_average}")
        #         break
            
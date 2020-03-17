"""
Escreva um programa completo que permita a qualquer aluno introduzir pelo tecla
do, uma sequência arbitrária de notas (válidas no intervao de 10 a 20) e que mos
tre na tela, como resultado, a correspondente média artimética. O número de no-
tas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa, o
qual terminará quando for introduzido um valor que não seja válido como nota de
aprovação.
"""

grades = []

while True:
    grade = input("Digite uma nota entre 10 e 20 : ")
    try:
        grade = float(grade)
    except:
        print("Digito inválido.")
    finally:
        if not grade >= 10 and grade <= 20:
            average = sum(grades) / len(grades)
            print(f"A média Artimetica das notas digitadas é : {round(average, 2)}")
        else:
            grades.append(grade)
            print(grades)
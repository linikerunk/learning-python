"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo
com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução
de conceito.
________________________________________________________________________________
|    NOTA     |    CONCEITO (ATÉ 20 FALTAS)    |   CONCEITO (MAIS DE 20 FALTAS)|
|-------------|--------------------------------|-------------------------------|
|9.0 Até 10.0 |                A               |                B              |
|7.5 Até 8.9  |                B               |                C              |
|5.0 Até 7.4  |                C               |                D              |
|4.0 Até 4.9  |                D               |                E              |
|0.0 Até 3.9  |                E               |                E              |
|------------------------------------------------------------------------------|
"""
while True:
    try:
        grade = input("Digite a nota do aluno : ")
        absent = input("Digite o número de falta do aluno : ")
        grande = float(grade)
        absent = int(absent)
    except:
        print("Valor inválido.")
    finally:
        if int(grade) < 0 or int(grade) > 10:
            print("Notá inválida.")
        elif int(grade) > 0 and int(grade) < 3.9:
            if int(absent) <= 20 and int(absent) > 0:
                print("Aluno está com Conceito E")
            elif int(absent) > 20:
                print("Aluno está com Conceito E")
            else:
                print("Falta negativa não válida")
        elif int(grade) >= 4.0 and int(grade) <= 4.9:
            if int(absent) <= 20 and int(absent) > 0:
                print("Aluno está com Conceito D")
            elif int(absent) > 20:
                print("Aluno está com Conceito E")
            else:
                print("Falta negativa não válida")
        elif int(grade) >= 5.0 and int(grade) <= 7.4:
            if int(absent) <= 20 and int(absent) > 0:
                print("Aluno está com Conceito C")
            elif int(absent) > 20:
                print("Aluno está com Conceito D")
            else:
                print("Falta negativa não válida")
        elif int(grade) >= 7.5 and int(grade) <= 8.9:
            if int(absent) < 20 and int(absent) > 0:
                print("Aluno está com Conceito B")
            elif int(absent) > 20:
                print("Aluno está com Conceito C")
            else:
                print("Falta negativa não válida")
        elif int(grade) >= 9.0 and int(grade) <= 10:
            if int(absent) <= 20 and int(absent) > 0:
                print("Aluno está com Conceito A")
            elif int(absent) > 20:
                print("Aluno está com Conceito B")
            else:
                print("Falta negativa não válida")
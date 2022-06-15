"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são
válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obriga-
toriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor
válido, este fato deve ser informado ao usuário eo programa termina 
"""

notas = []

while True:
    nota = input("Digite uma nota : ")

    try:
        nota = float(nota)
    except:
        print("Digito inválido.")
    finally:
        if nota < 0 or nota > 10:
            print("Nota inválido, valor deve estar entre 0.0 a 10.0")
        else:
            notas.append(nota)
            continuar = input("Deseja inserir uma outra nota : [SIM] ou [NAO] : ")
            try:
                continuar = str(continuar)
                continuar = continuar.upper()
            except:
                print("Valor inválido.")
            finally:
                if continuar == 'SIM':
                    pass
                elif continuar == 'NAO':
                    media = (sum(notas) / len(notas))
                    print(f"A média das notas é {media} ")
                    break
                else:
                    print("Digito inválido")
                    break

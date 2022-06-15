"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana
correspondente a este numero. Isto é, domingo se 1, segunda se 2, assim por diante. 
"""

while True:
    day_of_week = input("Digite um número para saber o dia da semana : ")
    def week(day_of_week):
            switcher = {
                0: "Não é um dia da semana",
                1: "Domingo",
                2: "Segunda-feira",
                3: "Terça-feira",
                4: "Quarta-feira",
                5: "Quinta-feira",
                6: "Sexta-feira",
                7: "Sábado",
            }

            if day_of_week in switcher:
                print(f" O dia {day_of_week} é {switcher[day_of_week]}")
            else:
                print("Digito inválido.")
    try:
        day_of_week = int(day_of_week)
    except:
        pass
    finally:
        week(day_of_week)
        
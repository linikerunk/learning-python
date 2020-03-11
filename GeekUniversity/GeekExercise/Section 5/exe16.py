"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.
"""

while True:
    digit = input("Digite um número para saber o mês correspondente : ")
    try:
        digit = int(digit)
    except:
        pass
    finally:
        def month(digit):
            switcher = {
                1: "Janeiro",
                2: "Fevereiro",
                3: "Março",
                4: "Abril",
                5: "Maio",
                6: "Junho",
                7: "Julho",
                8: "Agosto",
                9: "Setembro",
                10: "Outubro",
                11: "Novembro",
                12: "Dezembro",
            }

            if digit in switcher:
                print(f" O mês {digit} é {switcher[digit]}")
            else:
                print("Digito inválido.")

        month(digit)
    

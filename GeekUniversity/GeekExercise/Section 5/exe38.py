"""
Leia uma data de nascimento de uma pessoa fornecida atráves de três números
inteiros: Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma
data válida. Teste se o dia fornecido é um dia válido: dia >0, dia <= 28 para o
mês de fevereiro (29 se o ano for bissexto), dia 30 em abril, junho, setembro,
novembro, dia 31 nos outros meses, Teste a validade do mês > 0 e mês <13. Teste
a validade do ano: ano < ano atual (use uma constante definida como o valor
igual a 2020). Imprimir: "data válida" ou "data inválida" no final da execução
do programa.
"""

import datetime
DATE = datetime.datetime.now()

while True:
    birth = input("Digite sua data de nascimento [00/00/0000] : ")
    birth = birth.replace("/", "")
    birth_day =  birth[0:2];  birth_month = birth[2:4]; birth_year = birth[4:8]
    # print("Dia : ", birth_day, "Mes : ", birth_month, "Ano : ", birth_year)
    try:
        birth_day = int(birth_day)
        birth_month = int(birth_month)
        birth_year = int(birth_year)
    except:
        print("Data Inválida.")
    finally:
        if len(str(birth_year)) != 4:   #or int(birth_year) != DATE.year
            print("Data inválida.")
        else:
            if (int(birth_year) % 4 == 0 and int(birth_year) % 100 != 0 ) or int(birth_year) % 400 == 0:
                if int(birth_month) < 0 or int(birth_month) > 12:
                    print("Data inválida.")
                elif int(birth_month) == 2:
                    if int(birth_day) > 0 and int(birth_day) <= 29:
                        print("Data Válida.")
                    else:
                        print("Data Inválida.")
                elif int(birth_month) == 4 or int(birth_month) == 6 or int(birth_month) == 9 or int(birth_month) == 11:
                    if int(birth_day) > 0 and int(birth_day) <= 30:
                        print("Data Válida.")
                    else:
                        print("Data Inválida.") 
                else:
                    if int(birth_day) > 0 and int(birth_day) <= 31:
                        print("Data Válida.")
                    else:
                        print("Data Inválida.")
            else:
                if int(birth_month) < 0 or int(birth_month) > 12:
                    print("Data inválida.")
                elif int(birth_month) == 2:
                    if int(birth_day) > 0 and int(birth_day) <= 28:
                        print("Data Válida.")
                    else:
                        print("Data Inválida.")
                elif int(birth_month) == 4 or int(birth_month) == 6 or int(birth_month) == 9 or int(birth_month) == 11:
                    if int(birth_day) > 0 and int(birth_day) <= 30:
                        print("Data Válida.")
                    else:
                        print("Data Inválida.") 
                else:
                    if int(birth_day) > 0 and int(birth_day) <= 31:
                        print("Data Válida.")
                    else:
                        print("Data Inválida.")
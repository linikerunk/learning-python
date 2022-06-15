"""
Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está
entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em
anos bissextos, e 28 dias em anos não bissextos.
"""
import datetime
while True:
    date = input("Digite uma data válida : ")
    _format = "%d/%m/%Y"
    try:
        convert_date =  datetime.datetime.strptime(date, _format)
    except:
        print("Data Inválida.")
        break
    if len(str(convert_date.year)) > 4:
        print("Data Inválida year")
    elif int(convert_date.month) < 0 and int(convert_date.month) > 12:
        print("Data Inválida month")
    elif int(convert_date.day) <= 0 and int(convert_date.day) > 30:
        print("Data Inválida day")
    else:
        if int(convert_date.month) > 0 and int(convert_date.month) <= 1:
            if int(convert_date.day) > 0 and int(convert_date.day) <= 31:
                print("Data Válida.")
            else:
                print("Data Inválida.")
        elif int(convert_date.month) == 2:
            if int(convert_date.year) % 4 == 0 and int(convert_date.year) % 100 !=0 or int(convert_date.year) % 400 == 0:
                if int(convert_date.day) > 0 and int(convert_date.day) < 30:
                    print("Data Válida.")
                else:
                    print("Data Inválida.")
            else:
                if int(convert_date.day) > 0 and int(convert_date.day) < 29:
                    print("Data Válida.")
                else:
                    print("Data Inválida.")

        elif int(convert_date.month) > 2 and int(convert_date.month) <= 12:
            if int(convert_date.day) > 0 and int(convert_date.day) <= 31:
                print("Data Válida.")
            else:
                print("Data Inválida.")
        else:
            print("Data Inválida.")




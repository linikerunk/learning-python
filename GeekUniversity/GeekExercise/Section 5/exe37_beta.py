"""
As tarifas de certo parque de estacionamento são as seguintes :
    * 1 ª e 2 ª Hora - R$ 1,00 cada
    * 3 ª e 4 ª Hora - R$ 1,40 cada
    * 5 ª Hora - R$ 2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que paga
ria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e parti
da deste são apresentados na forma de pares de inteiros, representando horas e
minutos. Por exemplo, o par 12 50 representará "dez para a uma da tarde". Preten
de-se criar um programa que, lidos pelo teclado os momentos de chegada e de par-
tida, escreva na tela intervalo não superiror a 24 horas. Portanto, se uma dada
hora de chegada for superior à da partida, isso não é uma situação de erro, antes
significará que a partida ocorreu no dia seguinte ao da chegada.
"""

"""
separar problemas ( dividir para consquistar ):
    1 - separado em 12 50 == 12:50
    2 - não pode passar de 24:00
    3 - se a hora de entrada for superior a hora de saida significa que foi dado
    baixa no dia seguinte ex: 12:50  -> 11:50 -> 23Horas
    4 - passou 1 minuto a mais que 60 min já conta como se fosse 120 
"""

entrance = input("Digite a hora de entrada. [Exemplo 12:50] : ")
departure = input("Digite a hora de saída.  [Exemplo 13:50] : ")

entrance = entrance.replace(":", "")
departure = departure.replace(":", "")

if len(entrance) <= 4 and len(departure) <= 4:
    entrace_hour_initial = entrance[0:2]
    entrace_hour_final   = entrance[2:4]

    departure_hour_initial = departure[0:2]
    departure_hour_final   = departure[2:4]

    try:
        entrace_hour_initial, entrace_hour_final = int(entrace_hour_initial), int(entrace_hour_final)
        departure_hour_initial, departure_hour_final = int(departure_hour_initial), int(departure_hour_final)   
    except:
        print("Digito inválido.")
    finally:
        if  entrace_hour_initial > 24 or departure_hour_final < 0:
            print("Horário inválido > 24.")
        elif entrace_hour_final > 60 or entrace_hour_final < 0:
            print("Horário inválido. > 60")
        else:
            if  departure_hour_initial > 24 or departure_hour_initial < 0:
                print("Horário inválido. > 24")
            elif departure_hour_final > 60 or departure_hour_final < 0:
                print("Horário inválido. > 60")
            else:
                if departure_hour_initial > entrace_hour_initial:
                    hour_debit_initial = departure_hour_initial - entrace_hour_initial
                    if departure_hour_final > entrace_hour_final:
                        minute_debit_final = departure_hour_final - entrace_hour_final
                        if hour_debit_initial > 0 and hour_debit_initial <= 2:
                            if minute_debit_final > 0 and minute_debit_final < 60:
                                total_value = (hour_debit_initial + 1) * 1
                                print(f"Horário é {hour_debit_initial} : {minute_debit_final}")
                                print(f"Total a pagar é : {total_value}")
                                print("A")
                            elif minute_debit_final == 60:
                                minute_debit_final = 0
                                hour_debit_initial = hour_debit_initial + 1
                                print(f"Horário é {hour_debit_initial} : {minute_debit_final}")
                                print(f"Total a pagar é : {total_value}")
                                print("B")
                            else:
                                print("Horário inválido")
                    else:
                        minute_debit_final = abs((entrace_hour_final + 60) - departure_hour_final)
                        if minute_debit_final >= 60:
                            hour_debit_initial = departure_hour_final - entrace_hour_final
                            hour_debit_initial += 1
                            minute_debit_final = 0
                            print(f"Horário é {hour_debit_initial} : {minute_debit_final}")
                            print("C")
                        else:
                            hour_debit_initial -= 1
                            print(f"Horário é {hour_debit_initial} : {minute_debit_final}")
                            print("C")
                elif departure_hour_initial == entrace_hour_initial and departure_hour_final == entrace_hour_final:
                    hour_debit_initial = 24
                    minute_debit_final = 0
                    print(f"Horário é {hour_debit_initial} : {minute_debit_final}")
                    print("F")
                else:
                    hour_debit_initial = abs((entrace_hour_initial - departure_hour_initial) - 24)
                    if departure_hour_final > entrace_hour_final:
                        minute_debit_final = departure_hour_final - entrace_hour_final
                        print(f"Horário é {hour_debit_initial} : {minute_debit_final}")
                        print("D")
                    else:
                        minute_debit_final = abs((entrace_hour_final - 60) - departure_hour_final)
                        print(f"Horário é {hour_debit_initial} : {minute_debit_final}")
                        print("E")
                
else:
    print("Horário não existe")



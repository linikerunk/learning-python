"""
Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. Os funci
onário. Os funcionários com menor salário terão um aumento proporcionalmente 
maior do que os funcionários com um sálario maior, e conforme o tempo de serviço
na empresa, cada funionário irá receber um bônus adicional de salário. Faça um
programa que leia:
    * O valor do sálario atual do funcionário:
    * O tempo de serviço desse funcionário na empresa (número de anos de traba
    lho na empresa.)
Use as tabelas abaixo para calcular o sálario reajustado deste funcionário e im
prima o valor do salário final reajustado, ou uma mensagem caso o funcionário 
não tenha direito a nenhum aumento.

_______________________________________________________________________________________
|   Salário  Atual         |   Reajuste (%)   |    Tempo de serviço   |   Bonus       |
|--------------------------|------------------|-----------------------|---------------|
|   Até 500,00             |      25%         |    Abaixo de 1 ano    |   Sem bônus   |
|   Até 1000,00            |      20%         |    De 1 a 3 anos      |   100,00      |
|   Até 1500,00            |      15%         |    De 4 a 6 anos      |   200,00      |
|   Até 2000,00            |      10%          |    De 7 a 10 anos     |   300,00      |
|   Acima de 2000,00       |  Sem Reajuste    |    Mais de 10 anos    |   500,00      |
|__________________________|__________________|_______________________|_______________|
"""

salary = input("Digite o sálario do funcionário : ")
time_of_company = input("Digite o tempo de empresa do funcionário [1 -> ano] [0.1 - mês]: ")

try:
    salary, time_of_company = float(salary), float(time_of_company)
except:
    print("Digito inválido")
finally:
    if salary <= 500 and salary > 0:
        if time_of_company <= 1 and time_of_company > 0:
            salary = salary + (salary * 0.25)
            print(f"Sálario : {round(salary, 2)}")
            print("Sem bônus.")
        elif time_of_company > 1 and time_of_company < 4:
            salary = salary + (salary * 0.25) + 100
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 100,00, além do reajuste.")
        elif time_of_company >= 4 and time_of_company < 6:
            salary = salary + (salary * 0.25) + 200
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 200,00, além do reajuste.")
        elif time_of_company >= 7 and time_of_company <= 10:
            salary = salary + (salary * 0.25) + 300
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 300,00, além do reajuste.")
        elif time_of_company > 10:
            salary = salary + (salary * 0.25) + 500
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 500,00, além do reajuste.")
        else:
            print("Tempo de serviço não pode ser negativo.")
    elif salary > 500 and salary <= 1000:
        if time_of_company <= 1 and time_of_company > 0:
            salary = salary + (salary * 0.20)
            print(f"Sálario : {round(salary, 2)}")
            print("Sem bônus.")
        elif time_of_company > 1 and time_of_company < 4:
            salary = salary + (salary * 0.20) + 100
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 100,00, além do reajuste.")
        elif time_of_company >= 4 and time_of_company < 6:
            salary = salary + (salary * 0.20) + 200
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 200,00, além do reajuste.")
        elif time_of_company >= 7 and time_of_company <= 10:
            salary = salary + (salary * 0.20) + 300
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 300,00, além do reajuste.")
        elif time_of_company > 10:
            salary = salary + (salary * 0.20) + 500
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 500,00, além do reajuste.")
        else:
            print("Tempo de serviço não pode ser negativo.")
    elif salary > 1000 and salary <= 1500:
        if time_of_company <= 1 and time_of_company > 0:
            salary = salary + (salary * 0.15)
            print(f"Sálario : {round(salary, 2)}")
            print("Sem bônus.")
        elif time_of_company > 1 and time_of_company < 4:
            salary = salary + (salary * 0.15) + 100
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 100,00, além do reajuste.")
        elif time_of_company >= 4 and time_of_company < 6:
            salary = salary + (salary * 0.15) + 200
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 200,00, além do reajuste.")
        elif time_of_company >= 7 and time_of_company <= 10:
            salary = salary + (salary * 0.15) + 300
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 300,00, além do reajuste.")
        elif time_of_company > 10:
            salary = salary + (salary * 0.15) + 500
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 500,00, além do reajuste.")
        else:
            print("Tempo de serviço não pode ser negativo.")
    elif salary > 1500 and salary <= 2000:
        if time_of_company <= 1 and time_of_company > 0:
            salary = salary + (salary * 0.10)
            print(f"Sálario : {round(salary, 2)}")
            print("Sem bônus.")
        elif time_of_company > 1 and time_of_company < 4:
            salary = salary + (salary * 0.10) + 100
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 100,00, além do reajuste.")
        elif time_of_company >= 4 and time_of_company < 6:
            salary = salary + (salary * 0.10) + 200
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 200,00, além do reajuste.")
        elif time_of_company >= 7 and time_of_company <= 10:
            salary = salary + (salary * 0.10) + 300
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 300,00, além do reajuste.")
        elif time_of_company > 10:
            salary = salary + (salary * 0.10) + 500
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 500,00, além do reajuste.")
        else:
            print("Tempo de serviço não pode ser negativo.")
    elif salary > 2000:
        if time_of_company <= 1 and time_of_company > 0:
            print(f"Sálario : {round(salary, 2)}")
            print("Sem bônus.")
        elif time_of_company > 1 and time_of_company < 4:
            salary += 100 
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 100,00")
        elif time_of_company >= 4 and time_of_company < 6:
            salary += 200
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 200,00")
        elif time_of_company >= 7 and time_of_company <= 10:
            salary += 300
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 300,00")
        elif time_of_company > 10:
            salary += 500
            print(f"Sálario : {round(salary, 2)}")
            print("bônus de RS 500,00")
        else:
            print("Tempo de serviço não pode ser negativo.")
    elif salary < 0:
        print("Salário não pode ser negativo.")
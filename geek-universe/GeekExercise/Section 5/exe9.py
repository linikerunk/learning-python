"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso
contrário imprima: Empréstimo concedido.
"""

while True:
    salary = input("Digite seu sálario : ")
    parcel = input("Digite o valor da parcela do empréstimo : ")

    try:
        salary = float(salary)
        parcel = float(parcel)
    except:
        print("Digito Inválido")
    finally:
        salary_percentage = (salary * 0.2)
        if parcel > salary_percentage:
            print("EMPRÉSTIMO NÂO CONCEDIDO.")
        else:
            print("EMPRÉSTIMO CONCEDIDO.") 

        continuar = input("Deseja continuar -> [SIM] [NAO] : ")
        continuar = continuar.upper()

        if continuar == 'SIM':
            pass
        elif continuar == 'NAO':
            break
        else:
            print("Digito inválido, digite novamente...")
            continuar = input("Deseja continuar  -> [SIM] [NAO] : ")
            continuar = continuar.upper()
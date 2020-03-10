"""
A importância de R$ 780.000,00 será divida entre três ganhadores de um concurso.
Sendo que da quantia total:
    * O primeiro ganhador receberá 46%;
    * O segundo receberá 32%;
    * O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

premiacao = input(" Digite a premiação, caso aperte enter (premiacao = 780.000) : ")
print(premiacao)

try:
    if premiacao == '':
        premiacao = 780.000
        premiacao = float(premiacao)
    else:
        premiacao = float(premiacao)
    print(f" Primeiro ganhador : {round(premiacao * 0.46, 2)} \n \
         Segundo ganhador : {round(premiacao * 0.32, 2)} \n \
         Terceiro ganhador : {round(premiacao * (1 - (0.32 + 0.46)), 2)}")
except:
    print("Digito inválido..")
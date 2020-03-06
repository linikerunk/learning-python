"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    -not
Operadores bináros:
    -and, or, is

Regras de funcionamento: 
    Para o 'and', ambos os valores precisam ser True
    Para o 'or', um ou outro valor precisa ser True
    Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
    Para o 'is', o valor é comparado com um segundo valor.
"""

ativo = True
logado = False

if ativo and logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.")

if not ativo:
    print("Você precisa ativar sua conta. Check seu e-mail")
else:
    print("Bem-vindo Usuário.")

print(not(not(not(ativo))))

if ativo is False: # jeito pythonico é if not ativo:
    print("Você precisa ativar sua conta. Check seu e-mail")
else:
    print("Bem-vindo Usuário;")

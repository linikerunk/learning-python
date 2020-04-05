"""
o bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Previnindo assim que o programa para de funcionar e o usuário receba mensagens de erro
inesperadas.

A forma mais siples é:
try:
    //exceução mais problemática
except:
    // o que deve ser feito em caso de problema
"""
import sys


# Exemplo 1 - Trantando um erro genérico.
try:
    chamar_funcao_nao_existente()
except:
    print("Deu algum problema")

# Tente executar a função funcao() caso vc encontre erros imprima a mensagme de erro

# Exemplo 2 - Tratando um erro especifico.

try:
    liniker() # NameError
except NameError:
    print("Você está utilizando uma função inexistente")

# Exemplo 3 - Tratando um erro específico

try:
    len(5)
except TypeError as err:
    print(f"A aplicação gerou o seguinte erro: {err}")


try:
    #len(5)
    # nameerror()
    print('Liniker'[9])
except NameError as erra:
    print(f"Deu NameError: {erra}")
except TypeError as errb:
    print(f"Deu TypeError: {errb}")
except:
    print(f"Deu um erro diferente. {sys.exc_info()[0]}")


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Liniker"}

print(pega_valor(dic, "nome"))
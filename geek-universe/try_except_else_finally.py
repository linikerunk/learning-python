"""
Try/ Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

"""
#Else -> É executado somente se não ocorrer o erro.

# try:
#     num = int(input("Informe um número : "))
# except ValueError:
#     print("Valor incorreto.")
# else:
#     print(f"Você digitou {num}")

# # Finally

# try:
#     num = int(input("Informe um número : "))
# except ValueError:
#     print("Você não digitou um vlaor válido")
# else:
#     print(f"Você digitou o número {num}")
# finally:
#     print("Executando o finally.")

# #OBS: O bloco finally é sempre executado. Independente se houver exxceção ou não.

# # O finally geralmente é utilizado para fechar ou desalocar recursos.

# # Exemplo mais complexo errado

# def dividir(a, b):
#     return a / b

# num1 = int(input("Infome o primeiro número : "))
# try:
#     num2 = int(input("Infome o segundo número : "))
# except ValueError:
#     print("O valor precisa ser númerico.")
# try:
#     print(dividir(num1, num2))
# except NameError:
#     print("Valor incorreto")

# Exemplo mais complexo CORRETO
# OBS: você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return float(a) / float(b)
    except ValueError:
        return "Valor incorreto"
    except ZeroDivisionError:
        return "Não é possível realizar uma divisão por zero."

num1 = input("Infome o primeiro número : ")
num2 = input("Infome o segundo número : ")

print(dividir(num1, num2))

# Tratamento de erro semi-generico
def dividir(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um erro : {err}"

num1 = input("Infome o primeiro número : ")
num2 = input("Infome o segundo número : ")

print(dividir(num1, num2))
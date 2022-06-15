"""
Faça um program apra converter uma letra maíuscula em letra minúscula. Use a 
tabela ASCII para resolver o problema.
"""

letra = input("Digite uma letra para ser convertida para maiúscula: ")
letra = ord(letra)
print("a letra em maiúsculo é igual : ", chr(letra - 32))




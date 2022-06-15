"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples ->  'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas  ->  "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""


nome = """Geek University""" # or 'Geek University' or "Geek University"
print(nome)
print(type(nome))


nome2 = "Gina's Bar"
print(nome2)
print(type(nome2))


nome = 'Angelina "\nJolie'
print(nome)
print(type(nome))


nome = 'Geek University'
print(nome.upper())
print(nome.lower())
print(nome.split()) #transforma em uma lista de strings...

print("Geek University"[0:4]) #Slice de string
print(nome[5:15]) #Slice de string

# inverter a string
g
#Quero ir do primeiro elemento ir até o último elemento e inverta
print(nome[::-1]) # Método super pythonico.. IMPORTANTE

#Reverse só pode ser utilizado para listas
print(nome.replace('e', 'i'))
print(type(nome))


texto = "socorram me subino onibus em marrocos" # Palíndromo

print(texto)
print(texto[::-1])

nome = "Ana"
print(nome)
print(nome[::-1])
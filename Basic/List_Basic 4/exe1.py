# usando  expressoes regulares
import re  # regex

string_de_teste = ' O gato é bonito.'
# r'' -> RAW string tira os caracteres proprio da linguagem
padrao = re.search(r'gato', string_de_teste)

if padrao:
    print(padrao.group())  # search voce usao group para imprimir
else:
    print("Palavra não encontrada...")
print(r'Oi pessoa \n Segunda linha')

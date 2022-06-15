"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Virgulas

# Separador por virgula
1, 2, 3, 4, 5, 6
"geek", "university", "python

# Separador por ponto virgula
"geek"; "university"; "python

# Separador por espaço
1 2 3 4 5 6

"""

# Possível de se trabalhar, mas não é o idela..

# with open("lutadores.csv", encoding="utf8") as arquivo:
#     dados = arquivo.read()
#     dados = dados.split(",")[2:]
#     print(dados)

# A liguagem Python, possui duas formas diferentes para ler dados em arquivos CSV
#  - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
#  - DictReade -> Permite que iteremos sobre as linhas do arquivos CSV como 
# OrderedDicts;

# Reader 

from csv import reader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pular o cabeçalho, pois reader é um iterator
    print(type(leitor_csv))
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centimetros')
print("\n \n \nDictReader")
# DictReader

from csv import DictReader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura(em cm)']}")

# Com outro separador 

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=",")
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(
            f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura(em cm)']}")

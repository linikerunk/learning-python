"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:
num = 5

num < 5 
False

num < 10
True


NÃO EXISTE DO WHILE NO PYTHON .. 
do{
    //faça algo
}while(expressão);
"""

numero = 1

# Exemplo 1, cuidado com o loop infinito...
while numero < 10:
    print(numero)
    numero += 1

#OBS: Em um loop while, é importante que cuidemos do critério de parada.

# Exemplo 2 

resposta = ''

while resposta != "sim":
    resposta = input("Já acabou Jéssica? : ")
    resposta = resposta.lower()
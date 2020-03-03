"""
Escopo de variáveis

|------------------------------------| <- dentro do espaço é o escopo...

Dois casos de escopo:

1 - Variáveis Globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis Locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaras, ou seja, seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel - valor_da_variavel


Python é uma linguagem de tipagem dinânica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dado nela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = "Geek"
print(numero)
print(type(numero))


numero = 42

if numero > 50:
    novo = numero + 10 # A variável novo está declarada localmente dentro do bloco do IF, portanto é local.
    print(novo)

# print(novo) #Variável local pois não caiu na condição...


"""
Levantando os próprios erros com raise

raise -> Lança Exceções

OBS: O raise não é uma função. É uma palavra reservada. Assim como def ou qualquer outra
em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas
próprias exceções e mensagens de erros.

A Forma geral de utilização é :
raise TipoDoErro("Valor incorreto")

"""

# Exemplo real

def colore(texto, cor):
    cores = ('verde', 'vermelho', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string..")
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string..')
    print(f'O texto {texto} será impresso na cor {cor}')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')

colore("Liniker", 'roxo')

# OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise
# é executado.





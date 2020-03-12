"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes
conceitos:
    * O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
    * Chama-se equilátero o triângulo que tem o comprimento de dois lados iguais.
    * Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    * Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

side_a = input("Digite o primeiro lado do triângulo : ")
side_b = input("Digite o segundo lado do triângulo : ")
side_c = input("Digite o terceiro lado do triângulo : ")
try:
    side_a, side_b, side_c = float(side_a), float(side_b), float(side_c)
except:
    print("Digito inválido.")
finally:
    if not (side_c - side_b) < side_a and side_a < (side_c + side_b):
        print("Não podem ser valores dos lados de um triangulo. ")
    elif not (side_a - side_c) < side_b and side_b < (side_a + side_c):
        print("Não podem ser valores dos lados de um triangulo. ")
    elif not (side_a - side_b) < side_c and side_c < (side_a + side_b):
        print("Não podem ser valores dos lados de um triangulo. ")
    else:
        if side_a == side_b or side_a == side_c and side_b == side_c:
            print("Os valores digitados é de um triangulo equilátero.")
        elif side_a == side_b or side_b == side_c or side_c == side_a:
            print("Os valores digitados é de um triangulo isósceles.")
        else:
            print("Os valores digitados é de um triangulo escaleno.")
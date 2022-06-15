"""
Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
A área do circulo é PI * raio², considere PI = 3.141592
"""
PI = 3.141592

while True:
    try:
        raio = input("Digite o valor do raio : ")
        raio = float(raio)
        area = (PI * raio**2)
        print(f"A área do circulo é : {area}")
    except:
        print("Valor Inválido...")
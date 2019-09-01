#Faça um programa que receba o sexo como dado de entrada 
#e informe se o usuário é homem ou mulher.

sair = 1;
while sair != 0:
    nome = str(input("Digite seu Nome : "))
    nome = nome.capitalize()
    sexo = str(input("Digite seu Sexo [M] Masculino ou [F] Feminino : "))
    sexo = sexo[0].upper()
    if sexo == 'M': print(f"Olá {nome} você é do sexo → (Masculino).")
    elif sexo == 'F': print(f"Olá {nome} você é do sexo → (Feminino).")
    else:
        print('Valor do Sexo Inválido...')
        sexo = str(input("Digite seu Sexo Novamente [M] Masculino ou [F] Feminino : "))
    sair = int(input('Deseja sair ? Digite [0] p/ sair ou [1] para continuar: '))

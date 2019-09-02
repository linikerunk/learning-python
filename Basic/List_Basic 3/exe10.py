#Faça um programa para corrigir um teste de múltipla escolha com três questões.
#A resposta da primeira é "b" ou "B"; da segunda, "a" ou "A"; e da terceira,
#"c" ou "C". O programa conta um ponto a cada resposta correta.

################################################################################
#Painel para o Quiz...
import os

tela = ' Bem-Vindo ao Quiz de Naruto'
print('***'*10 + tela + '***'*10)

resposta1 = 0
while resposta1 != 'B':
    print('Quais das questões a seguir são um ataque do 4º Hokage : \n\
    (A) - [JAGEI JUBAKU], [RASENGAN], [CHIBAKU TENSEI] \n\
    (B) - [HIRAISHIN NO JUTSU], [SHIKI FUJIN], [RASENGAN] \n\
    (C) - [RASENGAN], [SENPOU: MYOJINMON], [KYUBI CHAKURA MODO] : ')
    resposta1 = input()
    resposta1 = str(resposta1.upper())
    if resposta1 == 'B':
        print('Parabéns você passou da primeira fase de conhecimento de Naruto... 33% Acerto..')
    if resposta1 != 'B':
        print('Você errou!!!! Jovem Genin treine mais seus conhecimentos sobre o Anime...')
os.system('cls')
resposta2 = 0
while resposta2 != 'A':
    print('\nCom quantos anos Uchiha Itachi se tornou capitão da ANBU : \n\
    (A) - 13 \n\
    (B) - 12 \n\
    (C) - 14  : ')
    resposta2 = input()
    resposta2 = str(resposta2.upper())

    if resposta2 == 'A':
        print(r'Parabéns você acertou, agora você está em 66,6 % de concluir o teste.')

    if resposta2 != 'A':
        print('Você errou!!!! Jovem Junin treine mais seus conhecimentos sobre o Anime...')

os.system('cls')
resposta3 = 0
while resposta3 != 'C':
    print('\nQuantos membros passaram pela organização Akatsuki [Considerando o MADARA] : \n \
    (A) - 11\n \
    (B) - 12\n \
    (C) - 13 : ')
    resposta3 = input()
    resposta3 = str(resposta3.upper())

    if resposta3 == 'C':
        print(r'Parabéns você acertou, Agora você já é um Hokage 100% de acertos..')

    if resposta3 != 'C':
        print('Você errou.. Sennin ainda falta essa para você se tornar um Hokage.')
os.system('cls')
print(' Você passou no Quiz de Naruto parábens..')
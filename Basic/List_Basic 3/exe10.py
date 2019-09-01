#Faça um programa para corrigir um teste de múltipla escolha com três questões.
#A resposta da primeira é "b" ou "B"; da segunda, "a" ou "A"; e da terceira,
#"c" ou "C". O programa conta um ponto a cada resposta correta.

################################################################################
#Painel para o Quiz...
tela = ' Bem-Vindo ao Quiz de Naruto'
print('***'*10 + tela + '***'*10)

print('Quais das questões a seguir são um ataque do 4º Hokage : \n\
(A) - [HIRAISHIN NO JUTSU], [SHIKI FUJIN], [RASENGAN] \n\
(B) - [JAGEI JUBAKU], [RASENGAN], [CHIBAKU TENSEI] \n\
(C) - [RASENGAN], [SENPOU: MYOJINMON], [KYUBI CHAKURA MODO] \n: ')
resposta1 = input()
resposta1 = str(resposta1.upper())
if resposta1 == 'A':
    print('Parabéns você passou da primeira fase de conhecimento de Naruto... 33% Acerto..')
if resposta1 != 'A':
    print('Você errou!!!! Jovem Genin treine mais seus conhecimento sobre o Anime...')
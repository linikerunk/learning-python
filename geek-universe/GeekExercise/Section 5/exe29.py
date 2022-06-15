"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aletórios entre 1 e 100, e mostre
na tela a pergunta: qual é a soma de a + b, onde a e b são os números  
aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as
respostas correstas, além de quantas vezes o aluno acertou.
"""
from random import randint

# print(randint(0, 100))

while True:
    numbers_a = randint(0, 100)
    numbers_b = randint(0, 100)

    question = input(f"Qual a soma de {numbers_a} + {numbers_b} : ")
    try:
        question = float(question)
    except:
        print("Digito inválido.")
    finally:
        anwser = numbers_a + numbers_b

        if question == anwser:
            print(f"Você acertou o número é : {anwser}")
        else:
            print(f"Você errou.. a resposta era : {anwser}")
# Escreva um programa que calcule o tempo de viagem de carro.
# Pergunte a distância a percorrer e a velocidade média para a viagem.

distancia = float(input("Qual a distância da viagem em KM : "))
tempo = float(input("Qual o tempo da viagem em horas : "))

print(f' A velocidade média da viagem foi : {distancia / tempo} Km/h')
conversao_metros = (distancia / tempo) / 3.6
print(f' A velocidade média da viagem em Metros por segundos foi : \
 {conversao_metros} m/s')
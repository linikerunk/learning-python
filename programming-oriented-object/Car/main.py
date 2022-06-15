# Learning Python OOP..

from veiculo import Veiculo
from carro import Carro


veiculo1 = Veiculo("Caminhão", "Preto", "FordCar", 12, 200) # posso colocar os parametros

#print(type(veiculo1)) <class 'veiculo.Veiculo'>

print(f"O veiculo criado é um {veiculo1.objeto}\n \
    Cor : {veiculo1.cor}.\n \
    Marca : {veiculo1.marca} \n \
    Qtn de Rodas : {veiculo1.rodas} \n \
    Capacidade do Tanque : {veiculo1.tanque}")

veiculo2 = Carro("Carro", "Azul", "Fiat", 4,
                   6)  # posso colocar os parametros
print(" \n \n  \t")
veiculo2.abastecer(100)
print(25*"*")

print(f"O veiculo criado é um {veiculo2.objeto}\n \
    Cor : {veiculo2.cor}.\n \
    Marca : {veiculo2.marca} \n \
    Qtn de Rodas : {veiculo2.rodas} \n \
    Capacidade do Tanque : {veiculo2.tanque}")


veiculo1.abastecer(500)

print(f"O veiculo criado é um {veiculo1.objeto}\n \
    Cor : {veiculo1.cor}.\n \
    Marca : {veiculo1.marca} \n \
    Qtn de Rodas : {veiculo1.rodas} \n \
    Capacidade do Tanque : {veiculo1.tanque}")

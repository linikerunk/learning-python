#Criando um Carro..


class Veiculo():

    def __init__(self, objeto, cor, rodas, marca, tanque):  # Construtor ...
        self.objeto = objeto
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque


    def abastecer(self, litros):
        self.tanque += litros
        print(f"Foi adicionado ao veiculo {self.objeto} {litros} Litros em seu tanque..")
        return self.tanque

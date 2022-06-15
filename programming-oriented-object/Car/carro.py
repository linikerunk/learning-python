from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, objeto, cor, marca, rodas, tanque):
        Veiculo.__init__(self, objeto, cor, rodas, marca, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 50 :
            print("Tanque cheio .. ")
        else:
            self.tanque += litros
            return self.tanque
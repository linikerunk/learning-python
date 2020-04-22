"""
Unittest - Antes e após hooks

-------
hooks são os teste em si. Ou seja a execução dos testes.
_______

setup() → é executado antes de cada método de teste. E util para criarmos instâncias
de objetos e outros dados;

tearDown() → é executado ao final de cada método de teste. E útil para excluir 
dados ou fechar conexões com bancos de dados.

"""
import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações dp setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def tearDown(self):
        # Configurações de tearDown()
        pass
    

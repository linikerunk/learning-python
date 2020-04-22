import unittest


from atividades import comer, dormir, engracada


class AtividadesTestes(unittest.TestCase):
    
    def test_comer_saudavel(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.')

    def test_comer_gostosa(self):
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.')

    def test_dormir_pouco(self):
        """ Testando o retorno dormingo pouco """
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )
    
    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Putz! Dormir muito! Estou atrasado para o trabalho!'
        )

    def test_engracada(self):
        # self.assertEqual(engracada('Sérgio Malandro'), False)
        self.assertFalse(engracada('Sérgio Malandro'))
        self.assertTrue(engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')


if __name__ == '__main__':
    unittest.main()


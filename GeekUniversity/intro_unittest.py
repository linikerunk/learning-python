"""
Introdução ao módulo Unittest

Unittest -> Test Unitários

O que são teste unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos etc.

OBS : Teste Unitários não estamos se referindo a Python, mas sim relacionado a 
desenvolvimento de código...

Para criar nossos testes, criamos classes que herdam de unittest.TestCase e a
partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os teste, utilizamos unittest.main()

TestCase -> Caso de test para sua unidade..

# Conhecendo as assertions

# Conhecendo as assertions
https://docs.python.org/3.3/library/unittest.html

Método                    Checa que
assertEqual(a, b)          a == b
assertNotEqual(a, b)       a != b
assertTrue(x)              x é verdadeiro
assertFalse(x)             x é false
assertIs(a, b)             a é b
assertIsNot(a, b)          a não é b
assertIfNone(a, b)         x é None
assertIsNotNone(a, b)      x não é None
assertIn(a, b)             a está em b
assertNotIn(a, b)          a não está em b
assertIsInstance(a, b)     a é instância de b
assertNotIsInstance(a, b)  a não é instância de b

Por convenção, todos os teste em um test case, devem ter seu nome iniciado com test_

# Para executar os testes com unittest

python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose
python nome_do_modulo -v

# Docstrings nos testes

Podemos acrescentar (e é recomendado) docstrings nos nossos testes.

# Prática - Utilizando a abordagem TDD

"""

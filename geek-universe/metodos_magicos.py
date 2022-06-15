"""
POO - Métodos Magicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

dunder init -> __init__()

Dunder -> Double Underscore

dunder repr -> Repersentação do objeto
"""

class Livro:

    def __init__(self, titulo, autor, pagina):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina
    
    def __repr__(self):# sobrescrevendo um métoodo mágico
        return f'{self.titulo} escrito por {self.autor}'
    
    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.pagina

    def __del__(self):
        return f'Um ojeto do tipo livro foi dletado da mémoria,'

    def __add__(self, outra):
        return f'{self} - {outra}'

    def __mul__(self, outra):
        if isinstance(outra, int):
            msg = ''
            for n in range(outra):
                msg += " " + str(self)
            return msg
        return "Nao posso multiplicar"

livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligencia Artificial com Python', 'Udemy', 500)

print(livro1 * 3)
print(livro1 + livro2)
print(len(livro1))
print(livro2)
print(livro1 * 'liniker')

class CisneNegro:

    def __len__(self):
        return 42

livro = CisneNegro()

print(len(livro))

nome = "Liniker"
lista = [12, 34, 35, 49]
dic = {"Liniker": 42, 'Vanessa': 56, "Joana": 49}


print(len(nome))
print(len(lista))
print(len(dic))


# idade = 42 # Nao vai dar certo pq nao é DuckTyping
# print(len(idade)) # Nao anda como a função
matrix = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^8}]', end="")# :^8 centralizar end="" manter na linha
    print()
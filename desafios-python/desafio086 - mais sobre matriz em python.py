print('------ DESAFIO 86 ------')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = coluna3 = segundamaior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
    print()

print('-=' * 30)

print(f'A soma dos valores pares é {somapares}')

for l in range(0, 3):
    coluna3 += matriz[l][2]

print(f'A soma dos valores da terceira coluna é {coluna3}')

for c in range(0, 3):
    if c == 0:
        segundamaior = matriz[1][c]
    elif matriz[1][c] > segundamaior:
        segundamaior = matriz[1][c]

print(f'O maior valor da segunda linha é {segundamaior}')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para [{linhas}, {colunas}]: '))
print('-=' * 20)
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matriz[linhas][colunas]:^5}]', end='')
    print()
for c in matriz:
    for a in c:
        if a % 2 == 0:
            soma += a
print(f'A soma de todos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
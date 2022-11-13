print('-'*44)
print(f'{"Listagem de Preços!":^45}')
print('-'*44)
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}|', end='')
    elif pos % 2 == 1:
        print(f'R${lista[pos]:>10}|')
print('-'*44)

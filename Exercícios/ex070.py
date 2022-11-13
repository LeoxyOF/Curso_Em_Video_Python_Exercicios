resp = cont = a = 0
soma = 0
barato = ''
baratocont = 0
print('-' * 20)
print('     CARREFOUR')
print('-' * 20)
while True:
    a += 1
    nome = str(input('Nome do Produto: ')).strip()
    preco = int(input('Preço do Produto: R$'))
    soma += preco
    resp = str(input('Quer continuar? '))[0].upper().strip()
    if resp != 'S' and resp != 'N':
        print('Resposta inválida!')
        while resp != 'S' and resp != 'N':
            resp = str(input('Quer continuar? '))[0].upper().strip()
    print('')
    if a == 1:
        barato = nome
        baratocont = preco
    if preco < baratocont:
        barato = nome
        baratocont = preco
    if preco > 1000:
        cont += 1
    if resp == 'N':
        break
print(f'O Total da compra foi R${soma:.2f}')
print(f'{cont} produtos custam mais que R$1000')
print(f'O produto mais barato foi {barato} custando R${baratocont:.2f}')

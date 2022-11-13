from time import sleep


def contador(inicio, final, passo):
    print('-~' * 20)
    print(f'Contando de {inicio} até {final} de {passo} em {passo}...')
    cont = inicio
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo += 1
        print('Passo inválido! foi convertido para 1')
    if inicio < final:
        while cont <= final:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += passo
        print()
    if inicio > final:
        while cont >= final:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= passo
        print()
    print('-~' * 20)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Início:  '))
f = int(input('Final:  '))
p = int(input('Passo:  '))
contador(i, f, p)

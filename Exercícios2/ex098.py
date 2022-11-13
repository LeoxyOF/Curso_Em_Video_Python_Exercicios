from time import sleep


def contador(inicio, final, passo):
    print('-' * 40)
    if passo < 0:
        print(f'{f"Contando de {inicio} até {final}, de {passo * -1} em {passo * -1}:":^5}')
    elif passo == 0:
        print(f'{f"Contando de {inicio} até {final}, de 1 em 1:":^5}')
    else:
        print(f'{f"Contando de {inicio} até {final}, de {passo} em {passo}:":^5}')
    if inicio > final and passo != 0:
        for cont in range(inicio, final - passo, - passo):
            print(f'[ {cont} ]', end='  ')
            sleep(0.5)
    elif inicio < final and passo != 0:
        for cont in range(inicio, final + passo, + passo):
            print(f'[ {cont} ]', end='  ')
            sleep(0.5)
    if passo < 0:
        for cont in range(inicio, final - (passo * -1), - (passo * -1)):
            print(f'[ {cont} ]', end='  ')
            sleep(0.5)
    if passo == 0:
        for cont in range(inicio, final - 1, - 1):
            print(f'[ {cont} ]', end='  ')
            sleep(0.5)

    print()
    print('-' * 40)


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
In = int(input('Início: '))
Fi = int(input('Final: '))
Pa = int(input('Passo: '))
contador(In, Fi, Pa)

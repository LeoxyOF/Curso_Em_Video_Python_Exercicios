from random import randint
from time import sleep
print('\033[36m-'*13)
print('Par ou ímpar')
print('-'*13)
cont = 0
while True:
    pc = randint(0, 10)
    resp = int(input('\033[33mEscolha um número: '))
    if resp > 10:
        print('\033[31mTem que ser um número menor que 10!')
        resp = int(input('\033[33mEscolha um número: '))
        if resp > 10:
            print('\033[31mPare de burlar o jogo ;-;')
            break
    paim = str(input('\033[35mPar ou Ímpar? '))[0].strip().upper()
    if paim != 'P' and paim != 'I':
        print('\033[31mResposta Inválida!')
        paim = str(input('\033[35mPar ou Ímpar? '))[0].strip().upper()
        if paim != 'P' and paim != 'I':
            print('\033[31mPare de burlar o jogo ;-;')
            break
    calcpar = (resp + pc) % 2
    print(f'\033[32mVocê = {resp}')
    sleep(0.5)
    print('\033[36mVS')
    sleep(1)
    print(f'\033[34mComputador = {pc}')
    sleep(1)
    if (resp + pc) % 2 == 0:
        print(f'\033[38m{resp + pc} é \033[36mPAR')
    elif (resp + pc) % 1 == 0:
        print(f'\033[38m{resp + pc} é \033[36mÌMPAR')
    if paim == 'P':
        if (resp + pc) % 2 == 0:
            print('\033[32mVocê Venceu!! :)')
            cont += 1
        elif (resp + pc) % 2 == 1:
            print('\033[31mVocê perdeu :(')
            break
    elif paim == 'I':
        if (resp + pc) % 2 == 1:
            print('\033[32mVocê Venceu!! :)')
            cont += 1
        elif (resp + pc) % 2 == 0:
            print('\033[31mVocê perdeu :(')
            break
if cont != 0 and cont != 1:
    print(f'\033[35mVocê teve um total de \033[38m{cont}\033[35m Vitórias!')
elif cont == 1:
    print('\033[35mVocê teve apenas \033[38m1\033[35m vitória!')
elif cont == 0:
    print('\033[35mVocê não teve nenhuma vitória \033[31m:(')
elif cont > 5:
    print(f'\033[36mParabéns!, Você teve um total de \033[38m{cont}\033[36m Vitórias!')
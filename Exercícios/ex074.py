from random import choice
from time import sleep
soma = ''
print('\033[1;33mOs números sorteados foram:\033[1;35m ', end='')
for c in range(0, 5):
    pc = choice('012345678910')
    soma += pc
    sleep(0.5)
    print(f'{pc} ', end='')
lista = sorted(soma)
print(f'\n\033[1;36mO menor valor é \033[1;39m{lista[0]}')
print(f'\033[1;34mO maior valor é \033[1;39m{lista[-1]}')

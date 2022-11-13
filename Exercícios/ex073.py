from time import sleep
times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Atlético-mg', 'Atlético-pr', 'Flamengo', 'Internacional',
         'Red bull bragantino', 'Santos', 'São paulo', 'Botafogo', 'Ceará', 'Goiás', 'Chapecoense', 'Avaí', 'Cuiabá',
         'Curitiba', 'Atlético-go', 'Juventude', 'Fortaleza')
print('\033[1;36mLista dos 20 primeiros colocados:')
for mostrar in times:
    print(f'\033[1;33m{mostrar}')
    sleep(0.3)
print('\033[39m-+='*13)
print('\033[1;31mOs 5 primeiros colocados são:')
for cont in range(0, 5):
    print(f'\033[1;35m{times[cont]}')
    sleep(0.6)
print('\033[39m-+='*13)
print('\033[1;34mOs últimos 4 colocados são:')
for cont2 in range(4, 0, -1):
    print(f'\033[1;32m{times[-cont2]}')
    sleep(0.6)
sleep(0.3)
print('\033[39m-+='*13)
print('\033[1;39mEm ordem alfabética fica:')
print(f'\033[1;33m{sorted(times)}')
sleep(1)
print('\033[39m-+='*13)
print(f'\033[31mO time do chapecoense está na posição \033[1;33m{times.index("Chapecoense")+1}')


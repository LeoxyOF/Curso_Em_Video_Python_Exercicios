pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = pri
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += raz
    cont += 1
print('FIM')

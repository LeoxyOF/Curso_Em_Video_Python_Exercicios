from math import factorial

#Usando o While

print('\033[1;33m===== Usando o While ===== \033[m')
num = int(input('\033[36mDigite um valor: '))
cont = num
print(f'\033[36mCalculando fatorial \033[39m{num}! ')
while cont > 0:
    print(f'\033[33m{cont}\033[31m', end='')
    cont -= 1
    if cont > 0:
        print('\033[31m x ', end='')
    else:
        if cont <= 1:
            print('\033[33m = ', end='')
print(f'\033[31m{factorial(num)}\033[m')

# Usando o for

print('')
print('===== Usando o for =====')
num = int(input('Digite o número: '))
f = 1
print(f'Fatorial de {num}!:')
for a in range (num, 0, -1):
    print(f'{a}', end='')
    if a > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= a
print(f)

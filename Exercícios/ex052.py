num = int(input('\033[1;33mDigite um Número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;33m', end='')
        tot += 1
    else:
        print('\033[1;31m', end='')
    print(f"{c} ", end='')
print(f'\n\033[1;34mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('\033[1;32mE por isso ele é PRIMO!')
else:
    print('\033[1;31mE por isso ele NÃO É PRIMO')

lista = []
for c in range(0, 5):
    lista.append(int(input(f'\033[1;39mDigite um valor para a posição \033[1;36m{c}\033[1;39m: ')))
print(f'\033[1;35mVocê digitou os valores: \033[1;37m{lista}')
print('\033[1;37m-=' * 20)
print(f'\033[1;34mo \033[1;39mMENOR\033[1;34m valor é \033[1;39m{min(lista)}\033[1;34m nas posições ', end='')
for a, b in enumerate(lista):
    if b == min(lista):
        print(f'\033[1;32m{a}', end='º ')
print(f'\n\033[1;33mE o \033[1;31mMAIOR\033[1;33m valor é \033[1;31m{max(lista)}\033[1;33m nas posições ', end='')
for c, d in enumerate(lista):
    if d == max(lista):
        print(f'\033[1;32m{c}', end='º ')

lista = (int(input('\033[1;36mDigite um valor: ')), int(input('\033[1;36mDigite um valor: ')),
         int(input('\033[1;36mDigite um valor: ')), int(input('\033[1;36mDigite um valor: ')))
print(f'\033[1;39mOs valores são: \033[1;36m{lista}')
if lista.count(9) == 1 and lista.count(9) != 0:
    print(f'\033[1;33mO número \033[1;31m9\033[1;33m aparece apenas \033[1;31m{lista.count(9)}\033[1;33m vez')
elif lista.count(9) > 1 and lista.count(9) != 0:
    print(f'\033[1;34mO número \033[1;31m9\033[1;34m aparece \033[1;31m{lista.count(9)}\033[1;34m vezes')
if 3 in lista:
    print(f'\033[1;35mO primeiro \033[1;31m3\033[1;35m digitado está na  '
          f'\033[1;31m{lista.index(3, 1)+1}º\033[1;35m posição')
cont = 0
for cada in lista:
    if cada % 2 == 0:
        cont += 1
if cont != 0 and cont != 1:
    print(f'\033[1;39mOs números pares são: ', end='')
if cont == 1:
    print(f'\033[1;39mO número par é: ', end='')
for cada in lista:
    if cada % 2 == 0:
        print(f'\033[1;32m{cada} ', end='')
        cont += 1

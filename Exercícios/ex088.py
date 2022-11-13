from random import randint
from time import sleep
cont = tot = 0
lista = []
jogos = []
print("-" * 30, f'\n{"Mega-Sena":^30}\n', "-" * 30)
resp = int(input('Jogos para sortear: '))
while tot < resp:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    cont = 0
    tot += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
for a, b in enumerate(jogos):
    print(f'Jogo Nª{a + 1}: {b}')
    sleep(1)

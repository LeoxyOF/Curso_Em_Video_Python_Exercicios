from random import randint
from time import sleep
from operator import itemgetter
dici = {}
ranking = {}
print("-=" * 3, "Valores Sorteados", "-=" * 3)
for c in range(1, 5):
    num = randint(1, 6)
    print(f'Jogador Nª{c} tirou: {num}')
    dici[F"Jogador Nª{c}"] = num
    sleep(1)
ranking = sorted(dici.items(), key=itemgetter(1), reverse=True)
print("-=" * 3, "Ranking", "-=" * 3)
for k, v in enumerate(ranking):
    print(f'{k+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)

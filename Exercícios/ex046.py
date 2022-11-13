from time import sleep
from emoji import emojize
print('\033[1;31m======== CONTAGEM PARA OS FOGOS DE ARTIFÍCIO! ========')
for contagem in range(10, 0, -1):
    print('\033[1;33m', contagem)
    sleep(1)
print('\033[1;33m 0')
print(emojize('\033[1;35mOS FOGOS ESTÃO ESTOURANDO!! :fireworks: :boom: :boom:', use_aliases='en'))
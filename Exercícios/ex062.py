pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = pri
cont = 1
resp = 10
total = 0
while resp != 0:
    total += resp
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += raz
        cont += 1
    print('Pausa')
    resp = int(input('Quantos termos você quer mostrar á mais? '))
if termo > 1:
    print(f'Progressão finalizada com sucesso, foram mostrados {termo} termos!')
else:
    print(f'Progressão finalizada com sucesso< foi mostrado apenas {termo} termo!')
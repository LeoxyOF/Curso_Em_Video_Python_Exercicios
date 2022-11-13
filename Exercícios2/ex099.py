from time import sleep
import random


def maior():
    """
    -> aleatoriza números aleatórios em quantidades aleatórias e os coloca
     dentro de uma lista e analisa os valores passados,
    e por fim, define o maior valor
    """
    maiorv = 0
    lista = []
    for abc in range(1, random.randint(0, 10)):
        while True:
            a = random.randint(0, 100)
            if a not in lista:
                lista.append(a)
                break
    for k, v in enumerate(lista):
        if k == 0:
            maiorv = v
        if v > maiorv:
            maiorv = v
    print(f'{"-="* 30}\n{"Analisando os valores passados...."}')
    for i in lista:
        print(i, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(lista)} valores ao todo\nO maior valor informado foi {maiorv}\n{"-=" * 30}')


while True:
    maior()
    while True:
        cont = str(input('Continuar? [S/N] >> ')).strip().upper()[0]
        if cont not in 'NS':
            print('Resposta inválida!')
        else:
            break
    if cont == 'N':
        print('<<< FIM >>>')
        help(maior)
        break

from random import randint
from time import sleep
numeros = []


def sorteie(lista):
    for cincovezes in range(0, 5):
        while True:
            aleatorizador = randint(0, 10)
            if aleatorizador not in lista:
                lista.append(aleatorizador)
                break

    print('Os valores sorteados foram ', end='')

    for valorsorteado in lista:
        print(valorsorteado, end=' ')
        sleep(0.5)


def somapar(lista):
    somadospares = 0

    for valor in lista:
        if valor % 2 == 0:
            somadospares = somadospares + valor

    print(f'\nSomando os valores pares de {lista} temos {somadospares}')


sorteie(numeros)
somapar(numeros)

def metade(num, fmt=False):
    if fmt:
        return moeda(num / 2)
    else:
        return num / 2


def dobro(num, fmt=False):
    if fmt:
        return moeda(num * 2)
    else:
        return num * 2


def aumentar(num, vzs, fmt=False):
    abc = 1.00 + (vzs / 100)
    if fmt:
        return moeda(num * abc)
    else:
        return num * abc


def diminuir(num, vzs, fmt=False):
    abc = 1.00 - (vzs / 100)
    calc = num * abc
    if fmt:
        return moeda(calc)
    else:
        return calc


def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')

def metade(num, fmt=False):
    if fmt:
        return f'R${num / 2:.2f}'
    else:
        return num / 2


def dobro(num, fmt=False):
    if fmt:
        return f'R${num * 2:.2f}'
    else:
        return num * 2


def aumentar(num, vzs, fmt=False):
    abc = 1.00 + (vzs / 100)
    if fmt:
        return f'R${num * abc:.2f}'
    else:
        return num * abc


def diminuir(num, vzs, fmt=False):
    abc = 1.00 - (vzs / 100)
    calc = num * abc
    if fmt:
        return f'R${calc:.2f}'
    else:
        return calc


def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')


def resumo(num, aum=0, dim=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{metade(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{aum}% de aumento: \t{aumentar(num, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(num, dim, True)}')
    print('-' * 30)


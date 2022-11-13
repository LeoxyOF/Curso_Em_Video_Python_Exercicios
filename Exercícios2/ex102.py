def fatorial(num, mostrar=False):
    """
    -> Calcúla Fatorial de número
        :param num: Número a ser calculado
        :param mostrar: (opcional) mostra calcúlo
        :return: Fatorial do num e os calcúlos se ativados
    """
    var = 1
    print(f'{num}! =', end=' ')
    for cont in range(num, 0, -1):
        var *= cont
        if mostrar:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print()
    return var


print(fatorial(int(input('Número: ')), mostrar=True))
help(fatorial)

from ex109 import moeda


def resumo(num, aum=0, dim=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda.moeda(num)}')
    print(f'Dobro do preço: \t{moeda.metade(num, True)}')
    print(f'Metade do preço: \t{moeda.metade(num, True)}')
    print(f'{aum}% de aumento: \t{moeda.aumentar(num, aum, True)}')
    print(f'{dim}% de redução: \t{moeda.diminuir(num, dim, True)}')
    print('-' * 30)

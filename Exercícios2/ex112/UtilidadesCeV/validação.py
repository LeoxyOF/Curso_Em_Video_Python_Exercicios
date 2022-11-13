from ex109.moeda import moeda

def resumo(num, aum=0, dim=0):
    print('-' * 30)
    print("RESUMO DO VALOR".center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{moeda(num * 2)}')
    print(f'Metade do preço: \t{moeda(num / 2)}')
    print(f'{aum}% de Aumento: \t{moeda(num * (1.00 + (aum / 100)))}')
    print(f'{dim}% de redução: \t{moeda(num * (1.00 - (dim / 100)))}')
    print('-' * 30)


def lerdinheiro(user):
    while True:
        cont = 0
        abc = str(input(user)).strip().replace(',', '.')
        for letras in abc:
            if letras.isnumeric():
                cont += 1
            if letras == '.':
                cont += 1
        if len(abc) == cont and abc != '':
            return float(abc)
        else:
            print(f'\033[1;31mERRO! "\033[m{abc}\033[1;31m" é um dado inválido!\033[m')

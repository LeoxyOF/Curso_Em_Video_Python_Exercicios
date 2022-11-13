

# parâmetro opcional e docstring
import math


def somar(a, b, c=0):
    """
    -> Soma dois ou três números
    :param a :
    :param b :
    :param c : (opcional)
    :return:
    """
    print(f'A soma é {a + b + c}')


somar(8, 12)

a = 2


# pegar variavél global e colocar no local
def teste():
    global a
    a = 5
    print(f'A dentro vale {a}')


teste()

print(f'A fora vale {a}')


# função com return
# retorna um resultado sem ter q printar
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(1, 2, 3)
r2 = somar(2, 8, 10)
r3 = somar(10, 14, 21)

print(f'A soma dos valores foi {r1}, {r2} e {r3}')


# exemplo
def factorial(num=0):
    s = 1
    print(f'{num}=', end=' ')
    for cont in range(num, 0, -1):
        s *= cont
        print(cont, end='')
        if cont > 1:
            print(' X ', end='')
        else:
            print('')
    return s


print(factorial(int(input('Digite um número:'))))


# outro exemplo
def parouimpar(a=0):
    if a % 2 == 0:
        return True
    else:
        return False


print(parouimpar(int(input('Detector de par:'))))
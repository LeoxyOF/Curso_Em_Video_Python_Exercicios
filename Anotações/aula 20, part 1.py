def lin():
    print('-' * 30)


lin()
print('   CURSO EM VÍDEO')
lin()
lin()
print('   APRENDA PYTHON')
lin()
print('   GUSTAVO GUANABARA')
lin()


def mensagem(msg):
    print('-' * (len(msg) + 5))
    print(f'{msg}')
    print('-' * (len(msg) + 5))


mensagem('ABACAXIDOMARNAREIADAPRAIA')


def soma(x, y, z):
    print(x - y * z)


soma(6, 7, 5)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [5, 2, 7, 9, 12]
print(valores)
dobra(valores)
print(valores)
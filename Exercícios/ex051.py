pt = int(input('\033[1;35mPrimeiro Termo: '))
rz = int(input('\033[1;36mRazão: '))
print(f'\033[1;33mOs Dez Primeiros Termos são: ', end='')
for a in range(pt, 10 * rz, rz):
    print('\033[1;36m', a, end=' / ')
print('\033[1;31mFim')

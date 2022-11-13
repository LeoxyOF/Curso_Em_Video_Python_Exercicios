while True:
    resp = int(input('Qual o valor para a tabuada? '))
    print(f'\033[1;39m-\033[m' * 33)
    if resp < 0 or resp == -0:
        break
    elif resp > 0:
        for cont in range(1, 11):
            print(f'\033[1;109m{resp} x {cont} = {resp * cont}\033[m')
    print(f'\033[1;39m-\033[m' * 33)
print('')
print('\033[31mPrograma encerrado!')

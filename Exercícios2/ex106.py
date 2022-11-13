def PyHELP():
    while True:
        print("\033[1;101;42m~" * 30)
        print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
        print("~" * 30)
        resp = str(input('\033[1;31;40mFunção ou biblioteca >> \033[m')).strip().lower()
        if resp != 'fim':
            abc = f'Acessando o manual do comando "{resp}"'
            print('\033[1;101;44m~' * (len(resp) + 40))
            print(f'{abc:^{len(resp) + 40}}')
            print('~' * (len(resp) + 40))
            print('\033[;101m')
            print('\033[1;40;37m')
            help(resp)
            print('\033[;101m')
        if resp == 'fim':
            print("\033[1;30;47m~" * 20)
            print(f'{"Até logo!":^20}')
            print("~" * 20)
            break


PyHELP()

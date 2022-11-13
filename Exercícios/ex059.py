def somar(x, y):
    return x + y


from time import sleep
esca = 0
pva = int(input('\033[36mDigite um valor: '))
sva = int(input('\033[36mDigite outro valor: '))
while esca != 5:
    print('''
\033[1;36m[1]\033[31m Somar
\033[1;36m[2]\033[1;31m Multiplicar 
\033[1;36m[3]\033[1;31m Maior
\033[1;36m[4]\033[1;31m Novos Números
\033[1;36m[5]\033[1;31m Sair do Programa''')
    sleep(0.5)
    print('')
    esca = int(input('\033[1;33mSua Escolha >> '))
    if esca == 1:
        print(f'\033[1;35mA soma dos valores \033[1;36m{pva} \033[1;35m+ \033[1;36m{sva} \033[1;35mresulta em \033[1;36m{somar(pva, sva)}')
    elif esca == 2:
        print(f'\033[1;35mA multiplicação dos valores \033[1;36m{pva}\033[1;35m x \033[1;36m{sva}\033[1;35m resulta em \033[1;36m{pva * sva}')
    elif esca == 3 and pva > sva:
        print(f'\033[1;35mO maior valor entre \033[1;36m{pva}\033[1;35m e \033[1;36m{sva} \033[1;35mé \033[1;36m{pva}')
    elif esca == 3 and sva > pva:
        print(f'\033[1;35mO maior valor entre \033[1;36m{pva}\033[1;35m e \033[1;36m{sva}\033[1;35m é \033[1;36m{sva}')
    elif esca == 3 and sva == pva:
        print(f'\033[39mOs valores são iguais!')
    elif esca == 4:
        pva = int(input('\033[36mDigite um Valor: '))
        sva = int(input('\033[36mDigite outro Valor:'))
    elif esca == 5:
        print('')
        print('\033[31mPrograma Finalizado!')
    else:
        if esca > 5:
            print('\033[31mEscolha Inválida!')
            sleep(0.5)
            print('\033[33mTente novamente!')
    sleep(1)
    print('')

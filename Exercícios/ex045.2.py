while True:
    import random
    from time import sleep
    comp = random.randint(1, 3)
    print('\033[1;31mPedra, Papel e Tesoura\033[m')
    print("""\033[1;33m
[1] Pedra
[2] Papel
[3] Tesoura\033[m
""")
    resp = int(input('\033[1;32mSua jogada >> \033[m'))
    print('')
    print('\033[1;31mJO')
    sleep(1)
    print('\033[1;31mKEN')
    sleep(1)
    print('\033[1;31mPÔ\033[1;33m!\033[m')
# Pedra
    if resp == 1 and comp == 1:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Pedra\n\033[1;35mComputador Escolheu Pedra\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;33mEmpate!\033[m')
    elif resp == 1 and comp == 2:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Pedra\n\033[1;35mComputador Escolheu Papel\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;31mVocê Perdeu!\033[m')
    elif resp == 1 and comp == 3:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Pedra\n\033[1;35mComputador Escolheu Tesoura\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;32mVocê Venceu!\033[m')
    elif resp == 1 and comp == 2:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Pedra\n\033[1;35mComputador Escolheu Papel\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;31mVocê Perdeu!\033[m')
    elif resp == 1 and comp == 3:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Pedra\n\033[1;35mComputador Escolheu Tesoura\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;32mVocê Venceu!\033[m')
# Papel
    if resp == 2 and comp == 2:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Papel\n\033[1;35mComputador Escolheu Papel\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;33mEmpate!\033[m')
    elif resp == 2 and comp == 1:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Papel\n\033[1;35mComputador Escolheu Pedra\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;32mVocê Venceu!\033[m')
    elif resp == 2 and comp == 3:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Papel\n\033[1;35mComputador Escolheu Tesoura\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;31mVocê Perdeu!\033[m')
# Tesoura
    if resp == 3 and comp == 3:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Tesoura\n\033[1;35mComputador Escolheu Tesoura\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;33mEmpate!\033[m')
    elif resp == 3 and comp == 2:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Tesoura\n\033[1;35mComputador Escolheu Papel\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;32mVocê Venceu!\033[m')
    elif resp == 3 and comp == 1:
        sleep(2)
        print('')
        print('\033[1;34m-='*13)
        print('\033[1;33mVocê Escolheu Tesoura\n\033[1;35mComputador Escolheu Pedra\033[m')
        print('\033[1;34m-='*13)
        sleep(2)
        print('')
        print('\033[1;31mVocê Perdeu!\033[m')
    print('')
    sleep(2)
    print('\033[1;33mReiniciando...')
    sleep(2)
    print('')

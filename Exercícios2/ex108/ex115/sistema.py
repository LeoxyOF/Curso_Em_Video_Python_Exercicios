licr = {
    'Amarelo': '\033[1;33m',
    'Azul': '\033[1;34m',
    'Verde': '\033[1;32m',
    "Vermelho": '\033[1;31m'
}


def colorir(txt, cor):
    return f'{cor}{txt}\033[m'


def opcao():
    while True:
        try:
            resp = int(input("\033[1;31mSua Opção: "))
            if resp > 3 or resp <= 0:
                print(f'{colorir("ERRO! digite um valor que esteja no menu!", licr["Vermelho"])}')
        except (KeyboardInterrupt, ZeroDivisionError):
            print('\n\033[1;31mO usuário preferiu não digitar o número\033[m')
            return 0
        except (TypeError, ValueError):
            print(f'\033[1;31mERRO! Digite um valor inteiro válido!!\033[m')
            continue
        else:
            return resp


def menu():
    lista = []
    while True:
        add = open('pessoas.txt', 'a')
        see = open('pessoas.txt', 'r')
        print('-' * 50)
        print('MENU PRINCIPAL'.center(50))
        print('-' * 50)
        print(f'{colorir("1", licr["Amarelo"])} - {colorir("Ver pessoas cadastradas", licr["Azul"])}')
        print(f'{colorir("2", licr["Amarelo"])} - {colorir("Cadastrar nova pessoa", licr["Azul"])}')
        print(f'{colorir("3", licr["Amarelo"])} - {colorir("Sair do sistema", licr["Azul"])}')
        print('-' * 50)
        cont = 0
        while True:
            try:
                while True:
                    resp = int(input("\033[1;32mSua Opção: \033[m"))
                    if 0 < resp <= 3:
                        break
                    print(f'{colorir("ERRO! digite um valor que esteja no menu!", licr["Vermelho"])}')
            except (KeyboardInterrupt, ZeroDivisionError):
                print('\n\033[1;31mO usuário preferiu não digitar o número\033[m')
                return 0
            except (TypeError, ValueError):
                print(f'\033[1;31mERRO! Digite um valor inteiro válido!!\033[m')
            else:
                if resp == 1:
                    print('-' * 50)
                    print('PESSOAS CADASTRADAS'.center(50))
                    print('-' * 50)
                    for v in see:
                        print(v)
                if resp == 2:
                    while True:
                        cont += 1
                        print("\033[1;33m-=" * 3, "CADASTRO", "-=" * 3, '\033[m')
                        nome = str(input(f'{colorir("Nome: ", licr["Azul"])}'))
                        while True:
                            try:
                                idade = int(input(f'{colorir("Idade: ", licr["Amarelo"])}'))
                            except (ValueError, TypeError):
                                print("\033[1;31mERRO! digite um valor inteiro válido!")
                            except KeyboardInterrupt:
                                print("\033[1;33mO usuário preferiu não informar a idade")
                            else:
                                if cont == 1:
                                    add.write(f"{nome}                             \t{idade} Anos")
                                else:
                                    add.write(f"\n{nome}                             \t{idade} Anos")
                                break
                        while True:
                            continuar = str(input(f"{colorir('Continuar? [S/N]: ', licr['Verde'])}")).strip().upper()[0]
                            if continuar not in 'NS':
                                print(f'\033[1;31mERRO! Por favor digite um valor válido!')
                            if continuar == 'S':
                                break
                            if continuar == 'N':
                                break
                        if continuar == 'S':
                            continue
                        if continuar == 'N':
                            break
                break


menu()
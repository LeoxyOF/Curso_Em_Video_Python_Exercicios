def lerint(inp):
    while True:
        try:
            resp = int(input(inp))
        except (KeyboardInterrupt, ZeroDivisionError):
            print('\n\033[1;31mO usuário preferiu não digitar o número\033[m')
            return 0
        except (TypeError, ValueError):
            print(f'\033[1;31mERRO! Digite um valor inteiro válido!!\033[m')
            continue
        else:
            return resp


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for key, valor in enumerate(lista):
        print(f"\033[33m{key + 1} \033[m- \033[34m{valor}\033[m")
    print(linha())
    opc = lerint("\033[1;32mSua Opção >> \033[m")
    return opc

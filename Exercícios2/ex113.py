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


def lerfloat(msg):
    while True:
        try:
            resp = float(input(msg))
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar o número\033[m')
            return 0
        except (TypeError, ValueError):
            print(f'\033[1;31mERRO! Digite um valor real válido!!\033[m')
            continue
        else:
            return resp


a = lerint('Inteiro: ')
b = lerfloat('Real: ')
print(f'O número inteiro é {a} e o real é {b}')

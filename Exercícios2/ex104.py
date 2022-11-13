def leiaint(resp):
    while True:
        a = str(input(resp)).strip()
        if a.isnumeric():
            return int(a)
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
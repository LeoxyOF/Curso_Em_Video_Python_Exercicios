from datetime import date
print('\033[1;31m-='*19)
print('\033[1;33m         Alistamento Militar')
print('\033[1;31m-='*19)
hoje = date.today().year
nasc = int(input('\033[1;33mQual é seu ano de nascimento? '))
idade = hoje - nasc
print(f'\033[1;35mQuem nasceu em \033[1;33m{nasc}\033[1;35m tem \033[1;33m{idade}\033[1;35m Anos em \033[1;33m{hoje}')
if idade == 18:
    print('\033[1;31mVocê tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'\033[1;34mAinda faltam \033[1;33m{saldo}\033[1;34m Ano(s) para o seu alistamento')
    falta = saldo + hoje
    print(f'\033[1;32mSeu alistamento será em \033[1;33m{falta}')
elif idade > 18:
    saldo = idade - 18
    print(f'\033[1;31mVocê já deveria ter se alistado á \033[1;33m{saldo}\033[1;31m Anos')
    falta = hoje - saldo
    print(f'\033[1;38mSeu alistamento foi em \033[1;33m{falta}\033[m')

from datetime import date
nasc = int(input('\033[1;33mQual é seu ano de nascimento? '))
idade = date.today().year - nasc
print(f'\033[1;37mVocê tem \033[1;36m{idade}\033[1;37m Anos')
if idade <= 9:
    print('\033[1;35mA sua categoria é MIRIM')
elif idade <= 14:
    print('\033[1;34mA sua categoria é INFANTIL')
elif idade <= 19:
    print('\033[1;36mA sua categoria é JUNIOR')
elif idade <= 20:
    print('\033[1;32mA sua categoria é SÊNIOR')
elif idade > 20:
    print('\033[1;31mA sua categoria é MASTER')

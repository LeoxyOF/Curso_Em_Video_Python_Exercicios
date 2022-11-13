pv = int(input('\033[1;33mPrimeiro Valor: '))
sv = int(input('\033[1;33mSegundo Valor: '))
if pv > sv:
    print('\033[1;32mO primeiro valor é maior')
elif sv > pv:
    print('\033[1;31mO segundo valor é maior')
elif pv == sv or sv == pv:
    print('\033[1;34mNão existe valor maior, os dois são iguais')

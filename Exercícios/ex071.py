print('-'*40)
print(" " * 14, 'Santander', " " * 20)
print('-'*40)
valor = int(input('Qual valor você deseja sacar? '))
ced = 50
total = valor
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

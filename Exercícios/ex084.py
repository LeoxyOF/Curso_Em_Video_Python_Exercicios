pri = []
seg = []
maior = menor = 0
while True:
    seg.append(str(input('Nome: ')).strip())
    seg.append(int(input('Peso: ')))
    if len(pri) == 0:
        maior = menor = seg[1]
    else:
        if seg[1] > maior:
            maior = seg[1]
        elif seg[1] < menor:
            menor = seg[1]
    pri.append(seg[:])
    seg.clear()
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Você cadastrou {len(pri)} pessoas')
print(f'O maior peso cadastrado foi {maior:.1f}Kg de', end=' ')
for c in pri:
    if c[1] == maior:
        print(f'{c[0]}', end='..')
print(f'\nE o menor peso cadastrado foi {menor:.1f}Kg de', end=' ')
for a in pri:
    if a[1] == menor:
        print(f'{a[0]}', end='..')

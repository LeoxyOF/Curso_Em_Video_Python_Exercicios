def texto(txt):
    print('~' * (len(txt) + 4))
    print(f'{txt:^{len(txt) + 4}}')
    print('~' * (len(txt) + 4))


while True:
    resp = str(input('Texto: ')).strip()
    texto(resp)
    cont = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if cont not in 'SN':
        print('Reposta inválida!!')
    if cont == 'N':
        break
print('<<< FIM >>>')



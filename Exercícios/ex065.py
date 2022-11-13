a = ''
cont = soma = maiorvalor = menorvalor = 0
while a != 'N':
    perg = int(input('Digite um número: '))
    cont += 1
    soma += perg
    a = str(input('Quer continuar? [N/S]: '))[0].strip().upper()
    if a != 'N' and a != 'S':
        print('\033[31mResposta inválida!\033[m')
    if cont == 1:
        maiorvalor = perg
        menorvalor = perg
    if cont > 1 and perg > maiorvalor:
        maiorvalor = perg
    if cont > 1 and perg < menorvalor:
        menorvalor = perg
media = soma / cont
if cont != 1:
    print(f'A média dos {cont} valores é {media:.1f}')
    print(f'O maior valor é {maiorvalor} e o menor é {menorvalor}')
else:
    print('Você digitou apenas um valor!')
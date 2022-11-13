comp = []
impar = []
par = []
while True:
    perg = int(input('Digite um valor: '))
    comp.append(perg)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp != 'N' and resp != 'S':
        while resp != 'N' and resp != 'S':
            resp = str(input('Resposta inválida! Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    if perg % 2 == 0:
        par.append(perg)
    else:
        impar.append(perg)
print(f'Você digitou os valores {comp}')
print(f'Os valores pares são: {par}')
print(f'E os valores ímpares são: {impar}')

resp = soma = cont = 0
while resp != 999:
    resp = int(input('Digite um número: '))
    if resp != 999:
        soma += resp
        cont += 1
if soma != 0:
    print(f'A soma dos {cont} valores foi {soma}')
else:
    print('Não tem nenhum valor!')

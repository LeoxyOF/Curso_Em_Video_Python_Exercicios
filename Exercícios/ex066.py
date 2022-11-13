n = soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        soma += n
    if n == 999:
        break
print(f'A soma dos {cont} valores é {soma}')

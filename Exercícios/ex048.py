soma = 0
cont = 1
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont += 1
print(f'\033[1;35mA soma dos {cont} valores solicitados é {soma}')

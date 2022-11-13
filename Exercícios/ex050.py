h = 0
for a in range(1, 7):
    resp = int(input(f'\033[1;33mDigite o Valor: N{a}\033[m'))
    if resp % 2 == 0:
        h += resp
print(f'\033[1;35mA soma dos valores foi {h}')
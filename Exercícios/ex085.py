lista = [[], []]
for c in range(1, 8):
    perg = int(input(f'Digite o {c}º valor: '))
    if perg % 2 == 0:
        lista[0].append(perg)
    else:
        lista[1].append(perg)
print(f'Pares: {sorted(lista[0])}\nÍmpares: {sorted(lista[1])}')

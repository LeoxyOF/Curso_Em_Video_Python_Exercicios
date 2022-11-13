def area(x, y):
    print(f'A área de [{x:.1f}] x [{y:.1f}] é {x * y:.1f}m²')


print('-' * 30)
print(f"{'Controle de Terreno':^30}")
print('-' * 30)
lar = float(input('Largura [m]: '))
comp = float(input('Comprimento [m]: '))

area(lar, comp)

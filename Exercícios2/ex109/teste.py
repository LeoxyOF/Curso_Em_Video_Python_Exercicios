from ex109 import moeda

p = float(input('Digite o preço R$'))

print(f'O Dobro do valor {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade do valor {moeda.moeda(p)} é {moeda.metade(p, True)}')
AUM = int(input('Aumentar quanto? '))
print(f'Aumentando {AUM}% de {moeda.moeda(p)} temos {moeda.aumentar(p, AUM, True)}')
DIM = int(input('Diminuir quanto? '))
print(f'Diminuindo {DIM}% de {moeda.moeda(p)} temos {moeda.diminuir(p, DIM, True)}')
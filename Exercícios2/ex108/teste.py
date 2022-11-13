from ex108.moeda import metade, dobro, dez, treze, moeda

p = float(input('Digite o preço R$'))

print(f'A metade desse valor é {moeda(metade(p))}')
print(f'O Dobro desse valor é {moeda(dobro(p))}')
print(f'Aumentando 10% temos {moeda(dez(p))}')
print(f'Diminuindo 13% temos {moeda(treze(p))}')

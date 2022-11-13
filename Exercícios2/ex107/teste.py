from ex107 import caixa

p = float(input('Digite o preço R$'))

print(f'A metade desse valor é {caixa.metade(p)}')
print(f'O Dobro desse valor é {caixa.dobro(p)}')
print(f'Aumentando 10% temos {caixa.dez(p)}')
print(f'Diminuindo 13% temos {caixa.treze(p)}')
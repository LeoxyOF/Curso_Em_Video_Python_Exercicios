import random
ab = random.randint(0, 300)
c = (ab-80)*7
print(f'O Carro estava á {ab} Kilômetros')
print(f'O Motorista irá pagar {c} Reais de Multa' if ab > 80 else 'Não teve Multas')
